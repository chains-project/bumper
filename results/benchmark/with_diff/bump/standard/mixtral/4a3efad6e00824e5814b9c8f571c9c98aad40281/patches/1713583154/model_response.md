Here's a possible patch for the code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;

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

// ...

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    // ...
    // PAdES parameters
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    // ...
    signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
    // ...
    // Create common certificate verifier
    CommonCertificateVerifier commonCertificateVerifier = new CommonCertificateVerifier();
    // Create PAdESService for signature
    PAdESService service = new PAdESService(commonCertificateVerifier);
    // ...
    // Get the SignedInfo segment that need to be signed.
    // respect local timezone
    DateTimeFormatter formatter = DateTimeFormatter.ISO_OFFSET_DATE_TIME.withZone(ZoneId.systemDefault());
    // user-provided timezone, if any
    if (params.getTimezone() != null) {
        formatter = formatter.withZone(ZoneId.of(params.getTimezone()));
    }
    // ...
    // ...
    ToBeSigned dataToSign = service.getDataToSign(toSignDocument, signatureParameters);
    // ...
    SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
    /* if (service.isValidSignatureValue(dataToSign, signatureValue, signingToken.getKey("alias").getCertificate())) {
    log.debug("is true");
    }
     */
    DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
    // ...
}
```

The patch removes the `CertificationPermission` import and replaces it with the fully qualified name `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED`.