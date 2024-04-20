Here's a proposed patch for the given error:

Change this line:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
to:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```

The issue is caused by the removal of the `CertificationPermission` class and its replacement with the `Permission` enum in the updated library. The `Permission` enum is now a nested enum within the `PAdESSignatureParameters` class.