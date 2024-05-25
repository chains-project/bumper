Here's a patch for the failing client code:

```java
import org.bouncycastle.tls.AlertDescription;

import java.security.GeneralSecurityException;
import java.security.Security;

public class ChachaDecoder {
    static {
        try {
            Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // ... (rest of the class remains unchanged)
}
```

This patch initializes the Bouncy Castle provider in a static block to ensure the external dependency is available before it's used in the class.