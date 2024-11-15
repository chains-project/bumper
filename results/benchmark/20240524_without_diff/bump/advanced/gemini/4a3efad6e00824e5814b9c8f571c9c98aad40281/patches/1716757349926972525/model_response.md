```java
import eu.europa.esig.dss.enumerations.CertificationPermission;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.validation.SignedDocumentValidator;

import java.io.IOException;
import java.nio.file.Path;
import java.security.KeyStore;
import java.security.KeyStore.PasswordProtection;
import java.util.logging.Logger;

public class Signer {

    private static final Logger log = Logger.getLogger(Signer.class.getName());

    public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
        // https://github.com/apache/pdfbox/blob/trunk/examples/src/main/java/org/apache/pdfbox/examples/signature/CreateVisibleSignature2.java
        // https://ec.europa.eu/cefdigital/DSS/webapp-demo/doc/dss-documentation.html
        // load PDF file
        // PDDocument doc = PDDocument.load(pdfFile.toFile());
        // load PDF file in DSSDocument format
        DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
        // load certificate and private key
        JKSSignatureToken signingToken = new JKSSignatureToken(keyStore, new PasswordProtection(keyStorePassword));
        log.debug("Keystore created for signing");
        // PAdES parameters
        PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
        // signatureParameters.bLevel().setSigningDate(new Date());
        String keyAlias = "alias";
        if (signingToken.getKeys().get(0) instanceof KSPrivateKeyEntry) {
            keyAlias = ((KSPrivateKeyEntry) (signingToken.getKeys().get(0))).getAlias();
        }
        signatureParameters.setSigningCertificate(signingToken.getKey(keyAlias).getCertificate());
        signatureParameters.setCertificateChain(signingToken.getKey(keyAlias).getCertificateChain());
        if (params.getUseTimestamp() || (!params.getTSA().isEmpty())) {
            signatureParameters.setSignatureLevel(SignatureLevel.PAdES_BASELINE_T);
        } else {
            signatureParameters.setSignatureLevel(SignatureLevel.PAdES_BASELINE_B);
        }
        signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
        // Create common certificate verifier
        CommonCertificateVerifier commonCertificateVerifier = new CommonCertificateVerifier();
        // Create PAdESService for signature
        PAdESService service = new PAdESService(commonCertificateVerifier);
        log.debug("Signature service initialized");
        // Initialize visual signature and configure
        if (params.getPage() != null) {
            SignatureImageParameters imageParameters = new SignatureImageParameters();
            TableSignatureFieldParameters fieldParameters = new TableSignatureFieldParameters();
            imageParameters.setFieldParameters(fieldParameters);
            if (!Strings.isStringEmpty(params.getImageFile())) {
                imageParameters.setImage(new InMemoryDocument(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(params.getImageFile()))));
            } else {
                imageParameters.setImage(new InMemoryDocument(org.apache.commons.io.IOUtils.toByteArray(getClass().getClassLoader().getResourceAsStream("signature.png"))));
            }
            if (params.getPage() < 0) {
                org.apache.pdfbox.pdmodel.PDDocument pdDocument = org.apache.pdfbox.pdmodel.PDDocument.load(toSignDocument.openStream());
                int pageCount = pdDocument.getNumberOfPages();
                fieldParameters.setPage(pageCount + (1 + params.getPage()));
                pdDocument.close();
                log.debug("PDF page count: " + pageCount);
            } else {
                fieldParameters.setPage(params.getPage());
            }
            fieldParameters.setOriginX((params.getLeft() * POINTS_PER_MM) * 10.0F);
            fieldParameters.setOriginY((params.getTop() * POINTS_PER_MM) * 10.0F);
            fieldParameters.setWidth((params.getWidth() * POINTS_PER_MM) * 10.0F);
            // Get the SignedInfo segment that need to be signed.
            // respect local timezone
            DateTimeFormatter formatter = DateTimeFormatter.ISO_OFFSET_DATE_TIME.withZone(ZoneId.systemDefault());
            // user-provided timezone, if any
            if (params.getTimezone() != null) {
                formatter = formatter.withZone(ZoneId.of(params.getTimezone()));
            }
            fieldParameters.setSignatureDate(formatter.format(signatureParameters.getSigningDate().toInstant()));
            fieldParameters.setSignaturString(signingToken.getKey(keyAlias).getCertificate().getSubject().getPrettyPrintRFC2253());
            if (!Strings.isStringEmpty(params.getHint())) {
                fieldParameters.setHint(params.getHint());
            } else {
                fieldParameters.setHint(Configuration.getInstance().getResourceBundle().getString("hint_text"));
            }
            signatureParameters.setImageParameters(imageParameters);
            PdfBoxNativeObjectFactory pdfBoxNativeObjectFactory = new PdfBoxNativeTableObjectFactory();
            service.setPdfObjFactory(pdfBoxNativeObjectFactory);
            log.debug("Visible signature parameters set");
        }
        // https://gist.github.com/Manouchehri/fd754e402d98430243455713efada710
        // only use TSP source, if parameter is set
        // if it is set to an url, us this
        // otherwise, default
        if (params.getUseTimestamp() || (params.getTSA() != null)) {
            CompositeTSPSource compositeTSPSource = new CompositeTSPSource();
            Map<String, TSPSource> tspSources = new HashMap<>();
            compositeTSPSource.setTspSources(tspSources);
            if (params.getTSA().isEmpty()) {
                Arrays.stream(Configuration.getInstance().getProperties().getStringArray("tsp_sources")).forEach((source) -> {
                    tspSources.put(source, new OnlineTSPSource(source));
                });
            } else {
                params.getTSA().stream().forEach((source) -> {
                    tspSources.put(source, new OnlineTSPSource(source));
                });
            }
            service.setTspSource(compositeTSPSource);
        }
        ToBeSigned dataToSign = service.getDataToSign(toSignDocument, signatureParameters);
        // This function obtains the signature value for signed information using the
        // private key and specified algorithm
        DigestAlgorithm digestAlgorithm = signatureParameters.getDigestAlgorithm();
        log.debug("Data to be signed loaded");
        SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
        /* if (service.isValidSignatureValue(dataToSign, signatureValue, signingToken.getKey("alias").getCertificate())) {
        log.debug("is true");
        }
         */
        log.debug("Signature value calculated");
        DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
        log.debug("Document signing complete");
        if (binary) {
            signedDocument.writeTo(System.out);
        } else {
            signedDocument.save(outputFile.toAbsolutePath().toString());
        }
    }
}
```