It seems that the `CertificationPermission` class has been removed from the latest version of the library. Here's a proposed patch to fix the error:
```java
public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    // ...
    // Remove the following line, as CertificationPermission has been removed
    // signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
    // ...
    eu.europa.esig.dss.pades.PAdESService service = new eu.europa.esig.dss.pades.PAdESService(commonCertificateVerifier);
    // ...
}
```
This patch removes the line that sets the `CertificationPermission` for the `PAdESService` instance. As the `CertificationPermission` class has been removed, this line is no longer needed.

Note that this patch assumes that the `CertificationPermission` class has been removed and that the `PAdESService` constructor does not require it as a parameter. If this is not the case, a different patch may be necessary.