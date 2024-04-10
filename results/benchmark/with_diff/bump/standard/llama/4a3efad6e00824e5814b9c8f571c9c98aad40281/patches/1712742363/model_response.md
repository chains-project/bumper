It seems that the error is caused by the removal of the `CertificationPermission` class in the new version of the library. To fix this error, you can replace the line:
```
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```
signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This will fix the error by importing the `CertificationPermission` enum from the `eu.europa.esig.dss.enumerations` package, which is not removed in the new version of the library.

Here's the full patch:
```
---

### main.java

---

72,43 : cannot find symbol
symbol:   variable CertificationPermission
location: class org.openpdfsign.Signer

---

72,43 : replace
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
with
signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);

---
```
This patch replaces the line `signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);` with `signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);` to fix the error caused by the removal of the `CertificationPermission` class in the new version of the library.