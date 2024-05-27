```java
import java.security.Provider;
import java.security.Security;

import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class ChachaDecoder {
    static {
        Provider bcProvider = new BouncyCastleProvider();
        Security.addProvider(bcProvider);
    }
    // rest of the class
}
```