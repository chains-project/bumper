Here's a potential patch for the failing client code:

```java
import org.bouncycastle.tls.AlertDescription;

import java.security.GeneralSecurityException;
import java.security.Security;

public class ChachaDecoder {
    // ...

    static {
        try {
            Security.addProvider(new BouncyCastleProvider());
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }

    // ...
}
```

This patch adds a static block that initializes the Bouncy Castle provider. This should ensure that the `org.bouncycastle.crypto.tls` package is available during runtime.

Note that this patch assumes that the Bouncy Castle JAR file is added to the classpath. If it's not, you'll need to add it first.