Here is the patched code:
```java
public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    // ...
    signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationLevel.MINIMAL_CHANGES_PERMITTED);
    // ...
}
```