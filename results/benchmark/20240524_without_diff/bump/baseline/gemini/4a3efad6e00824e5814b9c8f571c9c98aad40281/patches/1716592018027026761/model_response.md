```java
  import eu.europa.esig.dss.pades.CertificationPermission;
import eu.europa.esig.dss.pades.PAdESService;
import eu.europa.esig.dss.pades.signature.PAdESSignatureParameters;
import eu.europa.esig.dss.pades.signature.PAdESSigner;
import eu.europa.esig.dss.utils.Utils;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.security.GeneralSecurityException;
import java.security.KeyStore;
import java.security.PrivateKey;
import java.security.cert.Certificate;
import java.util.Collections;
import java.util.Date;

public class Signer {

    private static final String KEYSTORE_TYPE = "PKCS12";
    private static final String SIGNATURE_ALGORITHM = "SHA256withRSA";

    public static byte[] sign(byte[] data, String keystorePath, String keystorePassword, String alias, String pin) throws GeneralSecurityException, IOException {
        KeyStore keyStore = Utils.loadKeyStore(keystorePath, keystorePassword.toCharArray(), KEYSTORE_TYPE);
        PrivateKey privateKey = (PrivateKey) keyStore.getKey(alias, pin.toCharArray());
        Certificate[] chain = keyStore.getCertificateChain(alias);

        PAdESService padesService = new PAdESService(Collections.singletonList(new CertificationPermission()));
        PAdESSignatureParameters parameters = new PAdESSignatureParameters();
        parameters.setSigningCertificate(chain[0]);
        parameters.setBouncyCastleProvider(true);
        parameters.setSignatureAlgorithm(SIGNATURE_ALGORITHM);
        parameters.setSignatureProductionPlace("Europe");
        parameters.setSignatureProductionDate(new Date());

        PAdESSigner signer = padesService.newPAdESSigner(parameters, privateKey, chain);
        ByteArrayInputStream inputStream = new ByteArrayInputStream(data);
        ByteArrayOutputStream outputStream = new ByteArrayOutputStream();
        signer.sign(inputStream, outputStream, Collections.emptyMap());

        return outputStream.toByteArray();
    }
}
```