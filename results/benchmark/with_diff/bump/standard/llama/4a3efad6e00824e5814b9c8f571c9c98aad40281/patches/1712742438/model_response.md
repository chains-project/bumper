It seems that the `CertificationPermission` class has been removed from the latest version of the library. Here's a possible patch to fix the error:
```java
// Replace the line with the following code:
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);

// With:
signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This patch imports the `CertificationPermission` enum from the `eu.europa.esig.dss.enumerations` package, which is the same enum that was previously imported in the code. This should fix the error and allow the code to compile.

It's worth noting that the `CertificationPermission` enum has been removed from the latest version of the library, so you may need to update the code to use a different enum or class that provides similar functionality.