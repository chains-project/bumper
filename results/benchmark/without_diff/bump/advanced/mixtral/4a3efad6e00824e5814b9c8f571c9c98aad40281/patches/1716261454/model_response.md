Here's the proposed patch:

Replace the line with the error:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
It seems that the `CertificationPermission` enum has been moved to `eu.europa.esig.dss.pades.PAdESSignatureParameters` package, so you need to use the fully qualified name to fix the error.