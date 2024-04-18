Here is a possible patch for the given code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;
import org.openpdfsign.Signer;

import java.io.IOException;
import java.nio.file.Path;
import java.security.KeyStore;
import java.security.KeyStore.PasswordProtection;
import java.security.cert.Certificate;
import java.security.cert.CertificateChain;
import java.time.ZoneId;
import java.util.Map;

public void signPdf(Path pdfFile, Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws IOException {
    // ... (keep the original code, but replace CertificationPermission by eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission)
    signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);

    // ... (keep the original code)

    // Create PAdESService for signature
    PAdESService service = new PAdESService(commonCertificateVerifier);
    log.debug("Signature service initialized");

    // Initialize visual signature and configure
    if (visibleSignature) {
        // ... (keep the original code)

        // Get the SignedInfo segment that need to be signed.
        // respect local timezone
        java.time.format.DateTimeFormatter formatter = java.time.format.DateTimeFormatter.ISO_OFFSET_DATE_TIME.withZone(ZoneId.systemDefault());

        // ... (keep the original code)

        fieldParameters.setSignaturString(signingToken.getKey(keyAlias).getCertificate().getSubjectX500Principal().getName());

        // ... (keep the original code)
    }

    // ... (keep the original code)

    ToBeSigned dataToSign = service.getDataToSign(toSignDocument, signatureParameters);

    // This function obtains the signature value for signed information using the
    // private key and specified algorithm
    eu.europa.esig.dss.enumerations.DigestAlgorithm digestAlgorithm = signatureParameters.getDigestAlgorithm();
    log.debug("Data to be signed loaded");
    SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));

    log.debug("Signature value calculated");
    DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
    log.debug("Document signing complete");
    if (binary) {
        signedDocument.writeTo(System.out);
    } else {
        signedDocument.save(outputFile.toAbsolutePath().toString());
    }
}
```

This patch replaces the `CertificationPermission` class by the `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission` enum, which has a similar functionality. It also replaces the `getSubject().getPrettyPrintRFC2253()` method by `getSubjectX500Principal().getName()` method, which returns the same information in a different format.

Note that this patch assumes that the `SignatureParameters` class has a `getPage()` method that returns an `int` value, and that the `eu.europa.esig.dss.enumerations.SignatureLevel` enum has `PAdES_BASELINE_T` and `PAdES_BASELINE_B` constants. If these assumptions are not valid, the patch may need to be adjusted accordingly.