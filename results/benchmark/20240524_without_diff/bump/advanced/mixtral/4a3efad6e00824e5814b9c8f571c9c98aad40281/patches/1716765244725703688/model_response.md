Here's a proposed patch that should fix the error:

Replace the line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(new eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.PAdESSignaturePermission.MINIMAL_CHANGES_PERMITTED));
```
The issue is that the `CertificationPermission` class is not imported properly. However, instead of importing the class, we can directly use the `PAdESSignaturePermission` class from `eu.europa.esig.dss.pades.PAdESSignatureParameters` package, which has the same constant value `MINIMAL_CHANGES_PERMITTED`.