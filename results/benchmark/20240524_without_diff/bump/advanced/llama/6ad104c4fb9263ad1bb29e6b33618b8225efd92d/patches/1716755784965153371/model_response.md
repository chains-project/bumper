```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocketFactory;

import java.io.IOException;

public class ChachaDecoder {
    public void decode() throws IOException {
        Provider bcProvider = new org.bouncycastle.jce.provider.BouncyCastleProvider();
        Security.addProvider(bcProvider);
        SSLContext sslContext = SSLContext.getInstance("TLSv1.2");
        sslContext.init(null, null, null);
        SSLSocketFactory sslSocketFactory = sslContext.getSocketFactory();
    }
}
```