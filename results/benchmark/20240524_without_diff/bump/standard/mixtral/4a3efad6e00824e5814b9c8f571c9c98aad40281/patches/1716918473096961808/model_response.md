Here's the proposed patch:

Replace the line with the error:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(new eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission(eu.europa.esig.dss.pades.PAdESPermission.MINIMAL_CHANGES_PERMITTED));
```
The issue is that the `CertificationPermission` class was removed in a recent version of the dependency, and it has been replaced by the `Permission` class. The `Permission` class takes a `PAdESPermission` enum value as an argument.