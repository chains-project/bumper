Here's the fixed method with the required import statement added:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    DSSDocument toSignDocument = new FileDocument(pdfFile.toFile());
    eu.europa.esig.dss.token.JKSSignatureToken signingToken = new eu.europa.esig.dss.token.JKSSignatureToken(keyStore, new java.security.KeyStore.PasswordProtection(keyStorePassword));
    log.debug("Keystore created for signing");
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
    eu.europa.esig.dss.pades.CertificationPermission certificationPermission;
    if (visibleSignature) {
        certificationPermission = eu.europa.esig.dss.pades.CertificationPermission.MINIMAL_CHANGES_PERMITTED;
    } else {
        certificationPermission = eu.europa.esig.dss.pades.CertificationPermission.NO_CHANGES_ALLOWED;
    }
    signatureParameters.setPermission(certificationPermission);
    // ... rest of the method remains unchanged
}
```

The error was caused by the missing import statement for `CertificationPermission`, which is part of the `eu.europa.esig.dss.pades` package. I've added the import statement at the beginning of the method and replaced the `CertificationPermission` usage with its fully qualified name.