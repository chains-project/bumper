Here's a possible patch for the code that takes into account the new library version changes:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESService;
import eu.europa.esig.dss.token.JKSSignatureToken;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.openpdfsign.dss.PdfBoxNativeTableObjectFactory;
import org.openpdfsign.dss.SignerConstants;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.KeyStore;
import java.security.cert.Certificate;
import java.util.HashMap;
import java.util.Map;

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    // ... (previous code)
    // PAdES parameters
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    // ... (previous code)
    signatureParameters.setPermission(SignerConstants.CERT_PERMISSION_MINIMAL_CHANGES_PERMITTED);
    // ... (previous code)
    // Create PAdESService for signature
    PAdESService service = new PAdESService(commonCertificateVerifier);
    // ... (previous code)
    // Initialize visual signature and configure
    if (visibleSignature) {
        // ... (previous code)
        // Get the SignedInfo segment that need to be signed.
        // respect local timezone
        // ... (previous code)
        // fieldParameters.setSignaturString(signingToken.getKey(keyAlias).getCertificate().getSubject().getPrettyPrintRFC2253());
        fieldParameters.setSignaturString(signingToken.getKey(keyAlias).getCertificate().getSubjectX500Principal().getName());
        // ... (previous code)
    }
    // only use TSP source, if parameter is set
    // ... (previous code)
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
        signedDocument.writeTo(java.lang.System.out);
    } else {
        signedDocument.save(outputFile.toAbsolutePath().toString());
    }
}
```

The changes made are:

* Replace `CertificationPermission` with `SignerConstants.CERT_PERMISSION_MINIMAL_CHANGES_PERMITTED`.
* Replace `signingToken.getKey(keyAlias).getCertificate().getSubject().getPrettyPrintRFC2253()` with `signingToken.getKey(keyAlias).getCertificate().getSubjectX500Principal().getName()`.
* Import the necessary classes for the patch.
* Remove the unused import statements.

Note: I assumed that `SignerConstants` is a class that you have created, which contains the constant `CERT_PERMISSION_MINIMAL_CHANGES_PERMITTED`. If this is not the case, you may need to adjust the code accordingly.