Here's the proposed patch:

Change the following line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
to:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
This fixes the error by using the fully qualified name for `MINIMAL_CHANGES_PERMITTED`.