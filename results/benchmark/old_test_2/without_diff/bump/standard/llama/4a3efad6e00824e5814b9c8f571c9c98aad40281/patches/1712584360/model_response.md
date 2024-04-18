It seems that the `CertificationPermission` class is not available in the package `org.openpdfsign`. This class is part of the Java API, but it has been removed in Java 11.

To fix this issue, you can try using the `java.security.cert.CertificatePermission` class instead, which is the replacement for `CertificationPermission` in Java 11.

Here's a patch that you can apply to the code to fix this issue:
```diff
-        signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
+        signatureParameters.setPermission(java.security.cert.CertificatePermission.MINIMAL_CHANGES_PERMITTED);
```
This patch replaces the line that causes the error with a new line that uses the `java.security.cert.CertificatePermission` class instead of `CertificationPermission`.

After applying this patch, the code should compile without any errors related to the `CertificationPermission` class.