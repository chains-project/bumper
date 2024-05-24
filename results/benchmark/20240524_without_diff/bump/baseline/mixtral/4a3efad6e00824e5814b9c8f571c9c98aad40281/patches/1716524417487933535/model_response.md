Here is a possible patch for the client code:

```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

// ...

CertificationPermission permission = parameters.getPermission();
```

This patch imports the new location of the `CertificationPermission` enum and uses it to get the permission value from the `PAdESSignatureParameters` object.