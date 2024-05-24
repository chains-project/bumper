Here is a possible patch for the failing code:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

// ...

CertificationPermission permission = padesSignatureParameters.getPermission();
```

This patch imports the new `CertificationPermission` class from the `eu.europa.esig.dss.enumerations` package, and uses it to get the permission from the `PAdESSignatureParameters` object.

Note that the `getPermission()` method now returns a `CertificationPermission` object from the `eu.europa.esig.dss.enumerations` package, instead of a `CertificationPermission` object from the `eu.europa.esig.dss.pades` package.

This patch assumes that the `padesSignatureParameters` variable is an instance of the `PAdESSignatureParameters` class. If this is not the case, you may need to adjust the patch accordingly.