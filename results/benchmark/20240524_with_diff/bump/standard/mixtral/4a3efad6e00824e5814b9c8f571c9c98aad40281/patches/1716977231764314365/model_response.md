Here's the proposed patch:

Replace the line with the error:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
Explanation:

The error message indicates that the symbol `CertificationPermission` cannot be found, which suggests that the class `CertificationPermission` has been removed in the new library version.

The code should be updated to use the new fully qualified name `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission` instead of `CertificationPermission`. The `Permission` enum has a constant `MINIMAL_CHANGES_PERMITTED` that can be used to set the permission level.