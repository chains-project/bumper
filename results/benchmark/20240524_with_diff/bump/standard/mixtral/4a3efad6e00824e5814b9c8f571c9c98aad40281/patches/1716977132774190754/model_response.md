Here's a patch for the client code that should fix the error you encountered:

```java
import eu.europa.esig.dss.pades.CertificationLevel;

// ...

public void signPdf(java.nio.file.Path pdfFile, java.nio.file.Path outputFile, byte[] keyStore, char[] keyStorePassword, boolean binary, SignatureParameters params) throws java.io.IOException {
    boolean visibleSignature = params.getPage() != null;
    // ...
    eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
    // ...
    signatureParameters.setPermission(CertificationLevel.MINIMAL_CHANGES_PERMITTED);
    // ...
}
```

The error you encountered was that the `CertificationPermission` enum was removed in the new library version. It has been replaced by the `CertificationLevel` enum.

In the provided code, replace all occurrences of `CertificationPermission` with `CertificationLevel` and set the permission level accordingly.

Here's the updated line:

```java
signatureParameters.setPermission(CertificationLevel.MINIMAL_CHANGES_PERMITTED);
```