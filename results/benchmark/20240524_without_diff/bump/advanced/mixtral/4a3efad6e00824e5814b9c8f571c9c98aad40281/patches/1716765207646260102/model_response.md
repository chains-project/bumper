Here's the proposed patch:

Replace the line with the error with the following code:

```java
import eu.europa.esig.dss.pades.CertificatePolicyId;
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.PAdESSignatureParameters.PAdESSignatureParametersBuilder;

// ...

PAdESSignatureParametersBuilder builder = new PAdESSignatureParametersBuilder(signatureParameters);
builder.certificationPermission(CertificatePolicyId.CERT_POLICY_ID_316122);
signatureParameters = builder.build();
```

This code imports the necessary classes, creates a `PAdESSignatureParametersBuilder` instance, sets the `certificationPermission` to `CERT_POLICY_ID_316122`, and reassigns the `signatureParameters` variable with the updated values.

The `CertificatePermission` class has been replaced with `CertificatePolicyId` and the `CERT_POLICY_ID_MINIMAL_CHANGES_PERMITTED` constant has been replaced with `CERT_POLICY_ID_316122`.