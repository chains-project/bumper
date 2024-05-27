Here is the proposed patch:

Replace the line
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
This change should fix the error by using the fully qualified name of the `Permission` enum.