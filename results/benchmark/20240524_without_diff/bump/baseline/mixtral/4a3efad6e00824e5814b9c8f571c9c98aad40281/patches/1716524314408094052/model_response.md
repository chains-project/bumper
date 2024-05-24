Here's the proposed patch for the failing client code:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

// ...

CertificationPermission permission = parameters.getPermission();
```

In this patch, I replaced the import statement to use `eu.europa.esig.dss.enumerations.CertificationPermission` instead of the previous import from `eu.europa.esig.dss.pades`. This is because the `CertificationPermission` class is now located under the `eu.europa.esig.dss.enumerations` package.

I also updated the code to use the new `getPermission()` method from `PAdESSignatureParameters` which now returns `eu.europa.esig.dss.enumerations.CertificationPermission`.

This patch should resolve the "cannot find symbol" error related to `CertificationPermission`.