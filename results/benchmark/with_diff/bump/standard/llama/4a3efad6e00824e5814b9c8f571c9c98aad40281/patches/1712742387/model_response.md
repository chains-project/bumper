It seems that the `CertificationPermission` class has been removed from the latest version of the library. Here's a possible patch to fix the error:
```java
// Replace the line with the following code:
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);

// With:
signatureParameters.setPermission(new eu.europa.esig.dss.enumerations.CertificationPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED));
```
This patch creates a new instance of the `CertificationPermission` enumeration with the value `MINIMAL_CHANGES_PERMITTED`, which is the same value that was used in the original code. This should fix the error and allow the code to compile.


It's worth noting that the `CertificationPermission` enumeration has been removed from the latest version of the library, so you may need to update the code to use a different permission model. The `eu.europa.esig.dss.enumerations.CertificationPermission` class is still available in the latest version of the library, so you can use it to create a new instance of the `CertificationPermission` enumeration with the desired value.