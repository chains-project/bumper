The error message indicates that the variable `CertificationPermission` cannot be found. It seems like `CertificationPermission` is an enumeration that is not imported or doesn't exist in the current context. 

You need to replace `CertificationPermission.MINIMAL_CHANGES_PERMITTED` with `eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED` if the `CertificationPermission` enumeration is part of the `eu.europa.esig.dss.enumerations` package. 

Here is the corrected code snippet:

```java
public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    eu.europa.esig.dss.token.JKSSignatureToken signingToken = new eu.europa.esig.dss.token.JKSSignatureToken(keyStore, new java.security.KeyStore.PasswordProtection(keyStorePassword));
    log.debug("Keystore created for signing");
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
    signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
    eu.europa.esig.dss.validation.CommonCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();
    eu.europa.esig.dss.pades.signature.PAdESService service = new eu.europa.esig.dss.pades.signature.PAdESService(commonCertificateVerifier);
    log.debug("Signature service initialized");
    if (visibleSignature) {
        // ... rest of the code remains the same
    }
}
```