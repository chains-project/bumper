Here's the proposed patch to fix the error:

Replace the line:
`signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

With:
`signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);`

This patch updates the code to use the fully qualified name for the `MINIMAL_CHANGES_PERMITTED` constant, as the `CertificationPermission` class has been removed in the new library version.