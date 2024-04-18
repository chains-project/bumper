Here's the updated method with the required import for `CertificationPermission`:
```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;

//...

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    //...
    // PAdES parameters
    PAdESSignatureParameters signatureParameters = new PAdESSignatureParameters();
    //...
    signatureParameters.setPermission(eu.europa.esig.dss.pades.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
    //...
}
```
The `CertificationPermission` was moved from the package `org.openpdfsign` to `eu.europa.esig.dss.pades` in the updated library version.