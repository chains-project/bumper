Here's the proposed patch:

Replace the line with the error message with the following code:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
// ...
signatureParameters.setPermission(PAdESSignatureParameters.CertificationPermission.MINIMAL_CHANGES_PERMITTED);
```

This patch imports the missing class `CertificationPermission` from the `eu.europa.esig.dss.pades` package and uses it to set the permission for the signature parameters.