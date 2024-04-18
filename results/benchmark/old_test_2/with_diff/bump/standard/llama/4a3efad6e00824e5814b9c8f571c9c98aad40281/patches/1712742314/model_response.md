It seems that the `CertificationPermission` class has been removed in the new library version. You can fix this error by removing the reference to `CertificationPermission` and using a different class that provides the same functionality.


Here's a possible patch that you can apply to the code to fix the error:
```diff
- signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);
+ signatureParameters.setPermission(org.openpdfsign.Signer.Permission.MINIMAL_CHANGES_PERMITTED);
```
This patch replaces the reference to `CertificationPermission` with `org.openpdfsign.Signer.Permission`, which is a different class that provides the same functionality.

Note that this is just one possible solution, and you may need to adjust the code further to ensure that it compiles and runs correctly with the new library version.