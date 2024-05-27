Here's the proposed patch:

Replace the line that causes the error:
```java
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```java
signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);
```
Explanation:
The error message indicates that the `CertificationPermission` class is not found, which was likely removed in the new library version. Looking at the library changes, we can see that the `Permission` enum was added to the `eu.europa.esig.dss.pades.PAdESSignatureParameters` class. We can use this enum instead of the removed class.