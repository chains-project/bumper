In your code, it seems like `CertificationPermission.MINIMAL_CHANGES_PERMITTED` is not recognized. This could be due to a missing import statement or the class `CertificationPermission` is not available in the classpath. 

If `CertificationPermission` is a part of the `eu.europa.esig.dss.pades.PAdESSignatureParameters` package, you can try to replace `CertificationPermission.MINIMAL_CHANGES_PERMITTED` with `eu.europa.esig.dss.pades.PAdESSignatureParameters.CertificationPermission.MINIMAL_CHANGES_PERMITTED`. 

Here is the corrected code:

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
    signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
    eu.europa.esig.dss.validation.CommonCertificateVerifier commonCertificateVerifier = new eu.europa.esig.dss.validation.CommonCertificateVerifier();
    eu.europa.esig.dss.pades.signature.PAdESService service = new eu.europa.esig.dss.pades.signature.PAdESService(commonCertificateVerifier);
    log.debug("Signature service initialized");
    if (visibleSignature) {
        // ... rest of your code
    }
    // ... rest of your code
}
```
Be sure to check the correct fully qualified name for `CertificationPermission.MINIMAL_CHANGES_PERMITTED` in your project.