```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

public class ChachaDecoder {
    public ChachaDecoder() {
        String providerName = "BC";
        Provider bcProvider = new org.bouncycastle.jce.provider.BouncyCastleProvider();
        Security.addProvider(bcProvider);
        try {
            SSLContext sslContext = SSLContext.getInstance("TLS", providerName);
            sslContext.init(null, null, null);
        } catch (SSLException e) {
            // handle exception
        }
    }
}
```