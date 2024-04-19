Here's the proposed patch for the given code. I have imported the missing class `CertificationPermission` from the `eu.europa.esig.dss.pades` package:

```java
import eu.europa.esig.dss.pades.CertificationPermission;

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    // ...
    signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
    // ...
}
```

Add the above import statement at the beginning of the file to resolve the error.