Here's a potential patch for the failing client code:

```java
import org.bouncycastle.tls.AlertDescription;

import java.security.GeneralSecurityException;
import java.security.Provider;
import java.security.Security;
import java.util.Arrays;

public class ChachaDecoder {
    // ...

    static {
        Provider provider = Security.getProvider("BC");
        if (provider == null) {
            Security.addProvider(new BouncyCastleProvider());
        }
    }

    // ...
}
```

This patch adds a static block to initialize the BouncyCastleProvider if it is not already present in the security providers list. This should ensure that the `org.bouncycastle.crypto.tls` package is available at runtime.

Note that this patch assumes that the Bouncy Castle library is available on the classpath, but not necessarily initialized. If the library is not available at all, then a different solution may be required.