Here's the proposed patch:

Replace the line with the error:

`signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

with:

`signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);`

The issue is caused by the missing import statement for the `CertificationPermission` class. However, since you mentioned that we can only work on the client code and cannot change the function signature, the best solution is to replace the usage of `CertificationPermission` with the fully qualified version from the `eu.europa.esig.dss.pades` package.