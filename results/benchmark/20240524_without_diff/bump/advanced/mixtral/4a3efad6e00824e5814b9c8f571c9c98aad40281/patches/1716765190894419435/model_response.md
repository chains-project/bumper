Here's a proposed patch for the code:

Replace this line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
This patch imports the fully qualified name of the `MINIMAL_CHANGES_PERMITTED` constant from the `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission` class, which should resolve the "cannot find symbol" error.