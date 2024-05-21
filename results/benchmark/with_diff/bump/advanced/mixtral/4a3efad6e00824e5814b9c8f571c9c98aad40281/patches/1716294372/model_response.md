Here's the updated code with the necessary changes:

Replace:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
With:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
This change imports the correct `Permission` enum from the `eu.europa.esig.dss.pades` package instead of the removed `CertificationPermission` class.