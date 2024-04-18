It seems that the error is caused by the removal of the `CertificationPermission` class in the new library version. To fix this error, you can replace the line:
```
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```
signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This imports the `CertificationPermission` enumeration from the `eu.europa.esig.dss` package, which is not removed in the new library version.

Here's the full patch:
```
---

signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);

+++

signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);

```
This patch replaces the line `signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);` with `signatureParameters.setPermission(eu.europa.esig.dss.enumerations.CertificationPermission.MINIMAL_CHANGES_PERMITTED);` to fix the error caused by the removal of the `CertificationPermission` class in the new library version.