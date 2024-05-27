Here's the proposed patch:

Replace the line with the error:
`signatureParameters.setPermission(CertificationPermission.MINIMAL_CHANGES_PERMITTED);`

with:
`signatureParameters.setPermission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.MINIMAL_CHANGES_PERMITTED);`

Explanation:
The error message states that the symbol `CertificationPermission` cannot be found. This is because the class `CertificationPermission` is not imported in the code.

However, instead of importing the class, it's better to use the fully qualified name of the constant `MINIMAL_CHANGES_PERMITTED` from the class `eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission`. This way, the code becomes more readable and less prone to errors.