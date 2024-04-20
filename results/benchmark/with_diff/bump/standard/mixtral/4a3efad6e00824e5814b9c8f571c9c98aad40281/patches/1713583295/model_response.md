Here's a possible patch for the error you're encountering:

Replace the import statement for `CertificationPermission` with the following:
```java
import eu.europa.esig.dss.pades.CertificationPermission;
```
And replace the line that uses `CertificationPermission` with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This patch imports the `CertificationPermission` class from the correct package and fully qualifies its usage in the code.