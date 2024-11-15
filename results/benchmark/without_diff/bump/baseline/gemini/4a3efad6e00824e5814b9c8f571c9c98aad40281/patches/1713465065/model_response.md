```java
  import eu.europa.esig.dss.pades.CertificationPermission;
import eu.europa.esig.dss.pades.PAdESService;
import eu.europa.esig.dss.signature.SignaturePolicy;
import eu.europa.esig.dss.validation.CommonCertificateVerifier;
import org.bouncycastle.cms.CMSException;
import org.bouncycastle.tsp.TSPException;

import java.io.IOException;
import java.security.cert.X509Certificate;

public class Signer {

    public static byte[] sign(byte[] data, X509Certificate certificate, String pin) throws IOException, CMSException, TSPException {
        PAdESService padesService = new PAdESService(new CommonCertificateVerifier());
        padesService.setSignaturePolicy(SignaturePolicy.PADES_BASELINE_B);
        padesService.addSigner(certificate, pin, CertificationPermission.SIGN);
        return padesService.sign(data);
    }
}
```