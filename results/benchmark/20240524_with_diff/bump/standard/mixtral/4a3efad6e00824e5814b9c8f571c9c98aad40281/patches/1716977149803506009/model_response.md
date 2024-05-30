Here's a patch that you can apply to the code to fix the error:

Replace the line
`signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

with
`signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

Explanation:
The `CertificationPermission` enum has been moved from the `org.openpdfsign` package to the `eu.europa.esig.dss.pades` package in the new library version. Therefore, you need to use the fully qualified name of the enum to fix the error.