```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

import java.io.IOException;

public class ChachaDecoder {
    public ChachaDecoder() {
        String providerName = "BC";
        Provider provider = new org.bouncycastle.jce.provider.BouncyCastleProvider();
        Security.addProvider(provider);
    }
}
```