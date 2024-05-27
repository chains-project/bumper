Here's the updated code with the necessary changes:
```java
import eu.europa.esig.dss.pades.CertificationLevel;

// ...

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    // ...
    eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
    // ...
    signatureParameters.setPermission(CertificationLevel.MINIMAL);
    // ...
}
```
The necessary change is to replace the `CertificationPermission` import with `eu.europa.esig.dss.pades.CertificationLevel` and replace the `CertificationPermission` usage with `CertificationLevel.MINIMAL`.