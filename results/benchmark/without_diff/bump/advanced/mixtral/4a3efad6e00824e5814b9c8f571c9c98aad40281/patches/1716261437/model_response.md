Here's the proposed patch:

Replace the line with the error:
`signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

With:
`signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.CertificationPermission.MINIMAL_CHANGES_PERMITTED);`