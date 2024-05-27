```java
import java.security.Security;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

public class ChachaDecoder {
    public ChachaDecoder() {
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        try {
            SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
            sslContext.init(null, null, null);
        } catch (SSLException e) {
            throw new RuntimeException(e);
        }
    }
}
```