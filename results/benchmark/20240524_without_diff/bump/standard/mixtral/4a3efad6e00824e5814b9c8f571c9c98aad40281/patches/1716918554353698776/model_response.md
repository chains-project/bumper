Here's the proposed patch:

Replace the line with the error:

`signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

with:

`signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

In summary, the fully qualified name for `CertificationPermission` was used to fix the issue.