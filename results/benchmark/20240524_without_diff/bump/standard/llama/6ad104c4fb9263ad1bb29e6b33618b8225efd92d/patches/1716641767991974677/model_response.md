```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.KeyManagerFactory;
import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLServerSocketFactory;

import io.github.hapjava.server.impl.crypto.ChachaDecoder;

public class ChachaDecoder {
    public ChachaDecoder() {
        Provider bcProvider = new org.bouncycastle.jce.provider.BouncyCastleProvider();
        Security.addProvider(bcProvider);
    }
}
```