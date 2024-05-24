Here is a possible patch for the failing client code:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

//...

CertificationPermission permission = signatureParameters.getPermission();
```

This patch imports the new `CertificationPermission` class from the `eu.europa.esig.dss.enumerations` package, and uses it to get the permission from the `signatureParameters` object. Note that the `getPermission()` method now returns a `CertificationPermission` object, instead of a `CertificationPermission` object from the `eu.europa.esig.dss.pades` package.