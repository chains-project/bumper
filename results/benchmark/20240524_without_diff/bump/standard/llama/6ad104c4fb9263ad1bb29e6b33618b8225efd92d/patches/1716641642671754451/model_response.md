```java
import java.security.Security;
import javax.net.ssl.SSLContext;
import javax.net.ssl.TrustManagerFactory;

public class ChachaDecoder {
    public ChachaDecoder() {
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        SSLContext sslContext = SSLContext.getInstance("TLS");
        TrustManagerFactory trustManagerFactory = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());
        trustManagerFactory.init((javax.net.ssl.KeyManager[]) null);
        sslContext.init(null, trustManagerFactory.getTrustManagers(), null);
    }
}
```