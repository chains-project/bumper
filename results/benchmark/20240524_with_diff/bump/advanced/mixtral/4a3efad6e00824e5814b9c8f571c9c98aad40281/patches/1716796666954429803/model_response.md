Here's a possible patch for the error you're encountering:

Replace the import statement for `eu.europa.esig.dss.pades.CertificationPermission` with the following:
```java
import eu.europa.esig.dss.pades.PAdESCertificationLevel;
```
Then, replace the line that sets the `signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);` with the following:
```java
signatureParameters.setCertificationLevel(PAdESCertificationLevel.MINIMUM);
```
This should fix the "cannot find symbol" error you're encountering. Essentially, the `CertificationPermission` enum has been removed in the new library version and replaced with the `PAdESCertificationLevel` enum.