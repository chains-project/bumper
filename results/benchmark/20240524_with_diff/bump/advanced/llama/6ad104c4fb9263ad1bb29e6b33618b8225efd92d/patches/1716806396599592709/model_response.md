```java
import org.bouncycastle.jsse.BCSSLSocket;
import org.bouncycastle.jsse.BCSSLParameters;
import org.bouncycastle.jsse.provider.BouncyCastleJsseProvider;

import java.security.Security;

public class ChachaDecoder {
    public ChachaDecoder() {
        Security.addProvider(new BouncyCastleJsseProvider());
    }
}
```