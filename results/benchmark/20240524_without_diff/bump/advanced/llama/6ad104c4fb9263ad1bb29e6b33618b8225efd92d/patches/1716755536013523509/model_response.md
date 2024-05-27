```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

import java.io.IOException;

public class ChachaDecoder {
    public void decode() throws IOException, SSLException {
        String providerName = "BC";
        Provider bcProvider = new org.bouncycastle.jce.provider.BouncyCastleProvider();
        Security.addProvider(bcProvider);
        SSLContext sslContext = SSLContext.getInstance("TLS", providerName);
        // rest of the code
    }
}
```