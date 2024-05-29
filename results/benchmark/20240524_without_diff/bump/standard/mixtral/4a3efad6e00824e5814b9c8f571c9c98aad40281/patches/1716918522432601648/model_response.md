Here's the proposed patch:

Replace the line that causes the error:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
This change imports the `Permission` enum from the correct package.