```java
import java.security.Provider;
import java.security.Security;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class ChachaDecoder {
    static {
        Security.addProvider(new BouncyCastleProvider());
    }
    // ...
}
```