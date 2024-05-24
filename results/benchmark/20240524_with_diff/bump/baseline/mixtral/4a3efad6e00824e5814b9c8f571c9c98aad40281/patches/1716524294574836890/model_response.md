Here's a patch that you can apply to the client code to fix the error:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

// ...

CertificationPermission permission = padesSignatureParameters.getPermission();
```

This patch imports the new `CertificationPermission` class from the `eu.europa.esig.dss.enumerations` package, and uses it instead of the removed `CertificationPermission` class from the `eu.europa.esig.dss.pades` package. The `getPermission()` method of the `PAdESSignatureParameters` class has been changed to return a `CertificationPermission` object from the `eu.europa.esig.dss.enumerations` package, so this is a drop-in replacement for the original code.