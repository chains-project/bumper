Here's the proposed patch for the code:

Replace this line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
This change imports the `Permission` enum from the `eu.europa.esig.dss.pades` package instead of directly from `org.openpdfsign`. It seems that the `CertificationPermission` class was removed from the `org.openpdfsign` package, so we need to use the fully qualified name of the enum instead.