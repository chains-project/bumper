Here's a proposed patch for the given client code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;

import java.io.IOException;
import java.nio.file.Path;
import java.security.KeyStore;
import java.security.KeyStore.PasswordProtection;
import java.security.cert.Certificate;
import java.security.cert.CertificateChain;
import java.time.ZoneId;
import java.util.HashMap;
import java.util.Map;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    boolean visibleSignature = params.getPage() != null;
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    JKSSignatureToken signingToken = new JKSSignatureToken(keyStore, new PasswordProtection(keyStorePassword));
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    java.lang.String keyAlias = "alias";
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
    if (visibleSignature) {
        eu.europa.esig.dss.pades.SignatureImageParameters imageParameters = new eu.europa.esig.dss.pades.SignatureImageParameters();
        TableSignatureFieldParameters fieldParameters = new TableSignatureFieldParameters();
        imageParameters.setFieldParameters(fieldParameters);
        // ...
        fieldParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
        // ...
    }
    // ...
    eu.europa.esig.dss.pdf.PDFSignatureService service = new eu.europa.esig.dss.pdf.PDFSignatureService();
    // ...
    ToBeSigned dataToSign = service.getDataToSign(toSignDocument, signatureParameters);
    eu.europa.esig.dss.DigestAlgorithm digestAlgorithm = signatureParameters.getDigestAlgorithm();
    SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
    DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
    if (binary) {
        signedDocument.writeTo(System.out);
    } else {
        signedDocument.save(outputFile.toAbsolutePath().toString());
    }
}
```

The changes include:

1. Import the missing classes.
2. Replace `CertificationPermission` with `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED`.
3. Replace `eu.europa.esig.dss.pades.PAdESService` with `eu.europa.esig.dss.pdf.PDFSignatureService`, as the former is deprecated.
4. Create a new `eu.europa.esig.dss.pdf.PDFSignatureService` object, since it's not provided by the method parameters.
5. Replace `eu.europa.esig.dss.enumerations.DigestAlgorithm` with `eu.europa.esig.dss.DigestAlgorithm`, as the former is deprecated.

Please note that these changes are based on the latest version of the `dss` library (6.11.0). If you are using an older version, you may need to adjust the imports and class names accordingly.