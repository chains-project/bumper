Here's the fixed method with the necessary import statement added:
```java
import eu.europa.esig.dss.pades.CertificationPermission;

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    // load PDF file in DSSDocument format
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    // load certificate and private key
    eu.europa.esig.dss.token.JKSSignatureToken signingToken = new eu.europa.esig.dss.token.JKSSignatureToken(keyStore, new java.security.KeyStore.PasswordProtection(keyStorePassword));
    // PAdES parameters
    eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
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
    signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
    // Create common certificate verifier
    eu.europa.esig.dss.validation.CommonCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();
    // Create PAdESService for signature
    eu.europa.esig.dss.pades.signature.PAdESService service = new eu.europa.esig.dss.pades.signature.PAdESService(commonCertificateVerifier);
    // Initialize visual signature and configure
    if (visibleSignature) {
        // ...
    }
    // only use TSP source, if parameter is set
    if (params.getUseTimestamp() || (params.getTSA() != null)) {
        // ...
    }
    ToBeSigned dataToSign = service.getDataToSign(toSignDocument, signatureParameters);
    eu.europa.esig.dss.enumerations.DigestAlgorithm digestAlgorithm = signatureParameters.getDigestAlgorithm();
    SignatureValue signatureValue = signingToken.sign(dataToSign, digestAlgorithm, signingToken.getKey(keyAlias));
    DSSDocument signedDocument = service.signDocument(toSignDocument, signatureParameters, signatureValue);
    if (binary) {
        signedDocument.writeTo(java.lang.System.out);
    } else {
        signedDocument.save(outputFile.toAbsolutePath().toString());
    }
}
```
The only change made is adding the import statement for `CertificationPermission` at the beginning of the method.