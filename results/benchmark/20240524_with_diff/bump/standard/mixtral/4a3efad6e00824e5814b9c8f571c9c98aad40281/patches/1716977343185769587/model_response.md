Here's a possible patch that you can apply to the code to fix the error:

Replace the line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
This change should fix the error by using the fully qualified name of the `MINIMAL_CHANGES_PERMITTED` constant, which is now located in the `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission` class.