Here's the proposed patch for the failing client code:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

// ...

eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
// ...
signatureParameters.setPermission(CertificationPermission.CERTIFY_NEW_SIGNATURES);
```

The patch replaces the usage of `CertificationPermission` from `eu.europa.esig.dss.pades` package to `eu.europa.esig.dss.enumerations`. The `setPermission()` method's parameter has also been updated to the new `CertificationPermission` type.