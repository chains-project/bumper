Here's the proposed patch with the missing import statement added:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.enumerations.SignatureLevel;
import eu.europa.esig.dss.enumerations.DigestAlgorithm;
import eu.europa.esig.dss.spi.x509.tsp.CompositeTSPSource;
import eu.europa.esig.dss.spi.x509.tsp.TSPSource;
import eu.europa.esig.dss.spi.x509.tsp.OnlineTSPSource;
import eu.europa.esig.dss.model.DSSDocument;
import eu.europa.esig.dss.model.ToBeSigned;
import eu.europa.esig.dss.model.SignatureValue;
import eu.europa.esig.dss.pades.PdfBoxNativeObjectFactory;
import eu.europa.esig.dss.pades.TableSignatureFieldParameters;
import eu.europa.esig.dss.pades.SignatureImageParameters;
import eu.europa.esig.dss.pades.pdfbox.PdfBoxNativeTableObjectFactory;
import eu.europa.esig.dss.diagnostic.DiagnosticData;
import eu.europa.esig.dss.diagnostic.SignatureDiagnosticData;
import eu.europa.esig.dss.diagnostic.TimestampDiagnosticData;
import eu.europa.esig.dss.diagnostic.RevocationDiagnosticData;
import org.apache.pdfbox.pdmodel.PDDocument;
import org.apache.pdfbox.pdmodel.PDPage;
import org.openpdfsign.dss.PDFSignatureService;
import org.openpdfsign.dss.PDFSignatureServiceFactory;
import org.openpdfsign.Signer;
import org.openpdfsign.dss.SignerParameters;
import org.openpdfsign.dss.SignatureParameters;
import org.openpdfsign.dss.PDFSignatureServiceFactory;
import java.io.ByteArrayInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.charset.StandardCharsets;
import java.security.KeyStore;
import java.security.KeyStoreException;
import java.security.NoSuchAlgorithmException;
import java.security.cert.Certificate;
import java.security.cert.CertificateException;
import java.security.cert.CertificateFactory;
import java.util.Collection;
import java.util.Date;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    boolean visibleSignature = params.getPage() != null;
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    JKSSignatureToken signingToken = new JKSSignatureToken(keyStore, new KeyStore.PasswordProtection(keyStorePassword));
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    String keyAlias = "";
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
    CommonCertificateVerifier commonCertificateVerifier = new CommonCertificateVerifier();
    PAdESService service = new PAdESService(commonCertificateVerifier);
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
        } else {
            fieldParameters.setPage(params.getPage());
        }
        fieldParameters.setOriginX((params.getLeft() * Signer.POINTS_PER_MM) * 10.0F);
        fieldParameters.setOriginY((params.getTop() * Signer.POINTS_PER_MM) * 10.0F);
        fieldParameters.setWidth((params.getWidth() * Signer.POINTS_PER_MM) * 10.0F);
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
    SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
    DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
    if (binary) {
        signedDocument.writeTo(System.out);
    } else {
        signedDocument.save(outputFile.toAbsolutePath().toString());
    }
}
```

The missing import statement is:

`import eu.europa.esig.dss.pades.CertificationPermission;`