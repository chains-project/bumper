Here's the fixed method with the missing import statement added:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.spi.x509.tsp.CompositeTSPSource;
import eu.europa.esig.dss.spi.x509.tsp.TSPSource;
import eu.europa.esig.dss.enumerations.DigestAlgorithm;
import eu.europa.esig.dss.enumerations.SignatureLevel;
import eu.europa.esig.dss.enumerations.CertificatePolicyId;
import eu.europa.esig.dss.model.DSSDocument;
import eu.europa.esig.dss.model.InMemoryDocument;
import eu.europa.esig.dss.model.ToBeSigned;
import eu.europa.esig.dss.model.x509.CertificateToken;
import eu.europa.esig.dss.pades.SignatureImageParameters;
import eu.europa.esig.dss.pades.signature.PdfBoxNativeTableObjectFactory;
import eu.europa.esig.dss.pades.TableSignatureFieldParameters;
import org.openpdfsign.SignerParameters;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.security.KeyStore;
import java.security.KeyStore.PasswordProtection;
import java.security.cert.Certificate;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;
import java.util.HashMap;
import java.util.Map;
import java.util.stream.Stream;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignerParameters params) throws IOException {
    boolean visibleSignature = params.getPage() != null;
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    JKSSignatureToken signingToken = new JKSSignatureToken(keyStore, new PasswordProtection(keyStorePassword));
    log.debug("Keystore created for signing");
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    java.lang.String keyAlias = "alias";
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
    if (params.getPolicy() != null) {
        signatureParameters.setSigningCertificatePolicyId(CertificatePolicyId.forValue(params.getPolicy()));
    }
    signatureParameters.setPermission(params.getPermission() != null ? params.getPermission() : CertificationPermission.NO_CHANGES_ALLOWED);
    CommonCertificateVerifier commonCertificateVerifier = new CommonCertificateVerifier();
    PAdESService service = new PAdESService(commonCertificateVerifier);
    log.debug("Signature service initialized");
    if (visibleSignature) {
        SignatureImageParameters imageParameters = new SignatureImageParameters();
        TableSignatureFieldParameters fieldParameters = new TableSignatureFieldParameters();
        imageParameters.setFieldParameters(fieldParameters);
        if (!Strings.isStringEmpty(params.getImageFile())) {
            imageParameters.setImage(new InMemoryDocument(Files.readAllBytes(Paths.get(params.getImageFile()))));
        } else {
            imageParameters.setImage(new InMemoryDocument(IOUtils.toByteArray(getClass().getClassLoader().getResourceAsStream("signature.png"))));
        }
        if (params.getPage() < 0) {
            PDDocument pdDocument = PDDocument.load(toSignDocument.openStream());
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
        DateTimeFormatter formatter = DateTimeFormatter.ISO_OFFSET_DATE_TIME.withZone(ZoneId.systemDefault());
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
        PdfBoxNativeTableObjectFactory pdfBoxNativeObjectFactory = new PdfBoxNativeTableObjectFactory();
        service.setPdfObjFactory(pdfBoxNativeObjectFactory);
        log.debug("Visible signature parameters set");
    }
    if (params.getUseTimestamp() || (params.getTSA() != null)) {
        CompositeTSPSource compositeTSPSource = new CompositeTSPSource();
        Map<String, TSPSource> tspSources = new HashMap<>();
        compositeTSPSource.setTspSources(tspSources);
        if (params.getTSA().isEmpty()) {
            Stream.of(Configuration.getInstance().getProperties().getStringArray("tsp_sources")).forEach((source) -> {
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
    DigestAlgorithm digestAlgorithm = signatureParameters.getDigestAlgorithm();
    log.debug("Data to be signed loaded");
    SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
    log.debug("Signature value calculated");
    DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
    log.debug("Document signing complete");
    if (binary) {
        signedDocument.writeTo(System.out);
    } else {
        signedDocument.save(outputFile.toString());
    }
}
```