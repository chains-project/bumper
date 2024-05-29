Here's the proposed patch:

Replace the line with the error with the following code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission;

// ...

signatureParameters.setPermission(Permission.MINIMAL_CHANGES_PERMITTED);
```

This patch imports the necessary classes and uses the enum `Permission` from `PAdESSignatureParameters` instead of the removed `CertificationPermission`.