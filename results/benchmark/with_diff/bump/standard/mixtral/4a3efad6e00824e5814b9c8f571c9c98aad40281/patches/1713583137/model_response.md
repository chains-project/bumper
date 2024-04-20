Here's a patch to fix the error:

Replace the line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(new eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.CERTIFICATION_LEVEL.MINIMAL));
```
This fixes the error by using the fully qualified name for `Permission` and using the `CERTIFICATION_LEVEL` enum instead of `CertificationPermission`.