Here's the proposed patch:

Replace the line with the error message with the following code snippet:

```java
import eu.europa.esig.dss.pades.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.certificate.CertificateToken;
import eu.europa.esig.dss.pades.certificate.CertificateVerifier;
import eu.europa.esig.dss.pades.tsa.TSPSource;
import eu.europa.esig.dss.pades.tsa.TSPSourceFactory;
import eu.europa.esig.dss.pades.tsa.TimeStampTokenProvider;
import eu.europa.esig.dss.pades.tsa.TimeStampTokenProviderFactory;

// ...

eu.europa.esig.dss.pades.PAdESSignatureParameters signatureParameters = new eu.europa.esig.dss.pades.PAdESSignatureParameters();
// ...
CertificateVerifier cv = new CertificateVerifier();
cv.setCertificateToken(new CertificateToken(signingToken.getKey(keyAlias).getCertificate()));
cv.setCertificateChains(signingToken.getKey(keyAlias).getCertificateChain());
signatureParameters.setCertificateVerifier(cv);

// ...

TSPSource tspSource = TSPSourceFactory.getTspSource(params.getTSA());
if (params.getUseTimestamp()) {
    TimeStampTokenProvider tstProvider = TimeStampTokenProviderFactory.getTimeStampTokenProvider(tspSource);
    signatureParameters.setTimeStampTokenProvider(tstProvider);
}

// ...

signatureParameters.setPermission(new eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission(eu.europa.esig.dss.pades.PAdESSignatureParameters.Permission.PAdESSignatureParameters.Policy.MINIMUM_RESTRICTIONS));
```

This patch imports the necessary classes and modifies the code to use the `CertificateVerifier` and `TSPSource` classes instead of `CommonCertificateVerifier` and `CompositeTSPSource`. It also sets the permission with the `PAdESSignatureParameters.Permission` class instead of `CertificationPermission`.