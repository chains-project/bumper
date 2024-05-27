```java
import java.security.Provider;
import java.security.Security;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class ChachaDecoder {
    public ChachaDecoder() {
        Security.addProvider(new BouncyCastleProvider());
    }
    // ...
}
```