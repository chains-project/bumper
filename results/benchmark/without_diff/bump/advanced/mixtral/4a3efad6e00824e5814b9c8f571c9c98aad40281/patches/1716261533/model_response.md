Here's a possible patch that you can apply to fix the error:

Replace the line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
The error message indicates that the symbol `CertificationPermission` cannot be found, which suggests that the import statement for this class is missing. However, instead of adding the import statement, we can use the fully qualified name of the constant `MINIMAL_CHANGES_PERMITTED` from the `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission` class. This way, we avoid introducing a new dependency.