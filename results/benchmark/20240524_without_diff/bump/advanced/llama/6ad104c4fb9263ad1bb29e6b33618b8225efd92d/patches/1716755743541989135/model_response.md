```java
import java.security.Security;
import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManagerFactory;

import java.security.KeyManagementException;
import java.security.NoSuchAlgorithmException;

public class ChachaDecoder {
    public ChachaDecoder() {
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        try {
            SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
            sslContext.init(null, TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm()).getTrustManagers(), null);
        } catch (NoSuchAlgorithmException | KeyManagementException e) {
            throw new RuntimeException(e);
        }
    }
}
```