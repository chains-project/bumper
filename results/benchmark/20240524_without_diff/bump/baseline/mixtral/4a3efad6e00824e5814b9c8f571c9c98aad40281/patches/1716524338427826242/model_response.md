Here is the proposed patch:
```java
import eu.europa.esig.dss.enumerations.CertificationPermission;

// ...

CertificationPermission permission = signatureParameters.getPermission();
```
Explanation:
The `CertificationPermission` class has been removed from the `eu.europa.esig.dss.pades` package and has been moved to the `eu.europa.esig.dss.enumerations` package.

Therefore, you need to import `CertificationPermission` from the new package and update the import statement accordingly.

Additionally, the `getPermission()` method in the `PAdESSignatureParameters` class now returns `eu.europa.esig.dss.enumerations.CertificationPermission` instead of `eu.europa.esig.dss.pades.CertificationPermission`.

Therefore, you need to update the variable declaration to match the new return type.