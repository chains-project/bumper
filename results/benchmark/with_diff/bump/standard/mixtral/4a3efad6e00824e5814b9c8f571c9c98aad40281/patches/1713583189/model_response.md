Here's the proposed patch:

Replace the line that causes the error with the following code:
```java
signatureParameters.setPermission(new eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission(eu.europa.esig.dss.pades.PAdESObjectIdentifiers.PAdES_PERMIT_MINIMAL_CHANGES));
```
Explanation:

The error message indicates that the symbol `CertificationPermission` cannot be found. This is because the `CertificationPermission` enum has been removed in the new library version. Instead, we can use the `Permission` class and set the permission level using the `PAdES_PERMIT_MINIMAL_CHANGES` constant from the `PAdESObjectIdentifiers` class.