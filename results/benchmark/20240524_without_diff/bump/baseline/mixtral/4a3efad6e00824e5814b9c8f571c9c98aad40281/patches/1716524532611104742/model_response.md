Here's the proposed patch for the failing client code:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

// ...

CertificationPermission permission = parameters.getPermission();
```

In the provided library version changes, the `CertificationPermission` class has been moved from `eu.europa.esig.dss.pades` package to `eu.europa.esig.dss.enumerations`. So, you need to import it from the new package. Also, the `getPermission()` method now returns `eu.europa.esig.dss.enumerations.CertificationPermission` instead of `eu.europa.esig.dss.pades.CertificationPermission`. I have updated the code accordingly.