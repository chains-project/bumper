```java
import eu.europa.esig.dss.enumerations.CertificationPermission;
import java.io.IOException;
import java.nio.file.Path;
import java.security.KeyStore.PasswordProtection;
import java.util.Base64;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.Optional;
import java.util.Properties;
import java.util.stream.Arrays;
import java.util.stream.Collectors;
import org.apache.commons.io.IOUtils;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.apache.pdfbox.pdmodel.common.PDRectangle;
import org.apache.pdfbox.pdmodel.graphics.image.PDImageXObject;
import org.apache.pdfbox.pdmodel.interactive.annotation.PDAnnotation;
import org.apache.pdfbox.pdmodel.interactive.annotation.PDAnnotationWidget;
import org.apache.pdfbox.pdmodel.interactive.annotation.PDAppearanceDictionary;
import org.apache.pdfbox.pdmodel.interactive.annotation.PDAppearanceStream;
import org.apache.pdfbox.pdmodel.interactive.form.PDAcroForm;
import org.apache.pdfbox.pdmodel.interactive.form.PDField;
import org.apache.pdfbox.pdmodel.interactive.form.PDSignatureField;
import org.apache.pdfbox.rendering.PDFRenderer;
import org.apache.pdfbox.tools.imageio.ImageIOUtil;

public class Signer {

    public static final float POINTS_PER_MM = 0.3528F;
    private static final String SIGNATURE_FIELD_NAME = "Signature";
    private static final String SIGNATURE_FIELD_TYPE = "Sig";

    public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
        boolean visibleSignature = params.getPage() != null;

        // load PDF file
        PDDocument doc = PDDocument.load(pdfFile.toFile());

        // load certificate and private key
        eu.europa.esig.dss.token.JKSSignatureToken signingToken = new eu.europa.esig.dss.token.JKSSignatureToken(keyStore, new PasswordProtection(keyStorePassword));
        log.debug("Keystore created for signing");

        // PAdES parameters
        eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
        // signatureParameters.bLevel().setSigningDate(new Date());
        String keyAlias = "alias";
        if (signingToken.getKeys().get(0) instanceof eu.europa.esig.dss.token.KSPrivateKeyEntry) {
            keyAlias = ((eu.europa.esig.dss.token.KSPrivateKeyEntry) (signingToken.getKeys().get(0))).getAlias();
        }
        signatureParameters.setSigningCertificate(signingToken.getKey(keyAlias).getCertificate());
        signatureParameters.setCertificateChain(signingToken.getKey(keyAlias).getCertificateChain());
        if (params.getUseTimestamp() || (!params.getTSA().isEmpty())) {
            signatureParameters.setSignatureLevel(eu.europa.esig.dss.enumerations.SignatureLevel.PAdES_BASELINE_T);
        } else {
            signatureParameters.setSignatureLevel(eu.europa.esig.dss.enumerations.SignatureLevel.PAdES_BASELINE_B);
        }
        signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);

        // Create common certificate verifier
        eu.europa.esig.dss.validation.CommonCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();

        // Create PAdESService for signature
        eu.europa.esig.dss.pades.signature.PAdESService service = new eu.europa.esig.dss.pades.signature.PAdESService(commonCertificateVerifier);
        log.debug("Signature service initialized");

        // Initialize visual signature and configure
        if (visibleSignature) {
            eu.europa.esig.dss.pades.SignatureImageParameters imageParameters = new eu.europa.esig.dss.pades.SignatureImageParameters();
            TableSignatureFieldParameters fieldParameters = new TableSignatureFieldParameters();
            imageParameters.setFieldParameters(fieldParameters);
            if (!Strings.isStringEmpty(params.getImageFile())) {
                imageParameters.setImage(new InMemoryDocument(java.nio.file.Files.readAllBytes(java.nio.file.Paths.get(params.getImageFile()))));
            } else {
                imageParameters.setImage(new InMemoryDocument(IOUtils.toByteArray(getClass().getClassLoader().getResourceAsStream("signature.png"))));
            }
            if (params.getPage() < 0) {
                int pageCount = doc.getNumberOfPages();
                fieldParameters.setPage(pageCount + (1 + params.getPage()));
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
            PdfBoxNativeObjectFactory pdfBoxNativeObjectFactory = new org.openpdfsign.dss.PdfBoxNativeTableObjectFactory();
            service.setPdfObjFactory(pdfBoxNativeObjectFactory);
            log.debug("Visible signature parameters set");
        }

        // only use TSP source, if parameter is set
        // if it is set to an url, us this
        // otherwise, default
        if (params.getUseTimestamp() || (params.getTSA() != null)) {
            CompositeTSPSource compositeTSPSource = new CompositeTSPSource();
            Map<String, TSPSource> tspSources = new HashMap<>();
            compositeTSPSource.setTspSources(tspSources);
            if (params.getTSA().isEmpty()) {
                Arrays.stream(Configuration.getInstance().getProperties().getStringArray("tsp_sources")).forEach(( source) -> {
                    tspSources.put(source, new OnlineTSPSource(source));
                });
            } else {
                params.getTSA().stream().forEach(( source) -> {
                    tspSources.put(source, new OnlineTSPSource(source));
                });
            }
            service.setTspSource(compositeTSPSource);
        }
        ToBeSigned dataToSign = service.getDataToSign(new FileDocument(pdfFile.toFile()), signatureParameters);

        // This function obtains the signature value for signed information using the
        // private key and specified algorithm
        DigestAlgorithm digestAlgorithm = signatureParameters.getDigestAlgorithm();
        log.debug("Data to be signed loaded");
        SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
        log.debug("Signature value calculated");
        DSSDocument signedDocument = service.signDocument(new FileDocument(pdfFile.toFile()), signatureParameters, signatureValue);
        log.debug("Document signing complete");

        if (visibleSignature) {
            PDFRenderer renderer = new PDFRenderer(doc);
            PDPage page = doc.getPage(params.getPage());
            PDImageXObject image = renderer.renderImage(params.getPage(), 1.0F);

            PDAcroForm acroForm = doc.getDocumentCatalog().getAcroForm();
            if (acroForm == null) {
                acroForm = new PDAcroForm(doc, doc.getDocumentCatalog());
                doc.getDocumentCatalog().setAcroForm(acroForm);
            }

            PDSignatureField signatureField = new PDSignatureField(acroForm);
            signatureField.setName(SIGNATURE_FIELD_NAME);
            signatureField.setFieldType(SIGNATURE_FIELD_TYPE);
            signatureField.setValue(new PDSignatureField.Signature(Base64.getEncoder().encodeToString(signatureValue.getValue())));
            signatureField.setAppearance(new PDAppearanceDictionary());
            PDAppearanceStream appearanceStream = new PDAppearanceStream(doc);
            appearanceStream.setBBox(new PDRectangle(0, 0, image.getWidth(), image.getHeight()));
            appearanceStream.setContent(image.getImageBytes());
            signatureField.getAppearance().setNormalAppearance(appearanceStream);
            acroForm.getFields().add(signatureField);

            // add widget to page
            PDAnnotationWidget widget = new PDAnnotationWidget();
            widget.setRectangle(new PDRectangle(params.getLeft() * POINTS_PER_MM, params.getTop() * POINTS_PER_MM, params.getWidth() * POINTS_PER_MM, params.getHeight() * POINTS_PER_MM));
            widget.setPage(page);
            widget.setAnnotation(signatureField);
            widget.setFieldName(SIGNATURE_FIELD_NAME);
            page.getAnnotations().add(widget);
        }

        if (binary) {
            signedDocument.writeTo(System.out);
        } else {
            signedDocument.save(outputFile.toAbsolutePath().toString());
        }
    }
}
```