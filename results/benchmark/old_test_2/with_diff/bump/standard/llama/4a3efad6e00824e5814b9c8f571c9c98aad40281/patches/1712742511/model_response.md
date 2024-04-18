It seems that the `CertificationPermission` class has been removed from the latest version of the library. Here's a possible patch to fix the error:
```java
// Replace the line with the following code:
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);

// With:
signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This patch replaces the reference to the removed `CertificationPermission` class with the equivalent enumeration value from the `eu.europa.esig.dss.enumerations` package. This should fix the compilation error and allow the code to run with the updated library version.