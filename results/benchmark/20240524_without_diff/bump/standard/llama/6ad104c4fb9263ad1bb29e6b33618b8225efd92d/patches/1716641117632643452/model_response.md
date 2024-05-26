```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class ChachaDecoder {
    public ChachaDecoder() {
        Security.addProvider(new BouncyCastleProvider());
    }
}
```