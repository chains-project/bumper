It seems that the error is caused by the removal of the `CertificationPermission` class in the new version of the library. To fix this error, you can replace the line:
```
signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
with:
```
signatureParameters.setPermission(java.security.CryptoPrimitive.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This will fix the error by using the `CryptoPrimitive` class from the `java.security` package, which is not affected by the library changes.


Here's the full patch:
```diff
-signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
+signatureParameters.setPermission(java.security.CryptoPrimitive.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```
This patch replaces the line 72 in the provided code with the new line, which uses the `CryptoPrimitive` class to set the permission.