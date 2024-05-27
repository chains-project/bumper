Here's a proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.security.Security;

public class ChachaDecoder {
    // ...

    static {
        // Add the Bouncy Castle provider to the security providers list
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
    }

    // ...
}
```
The patch initializes the Bouncy Castle provider in a static block, which ensures that the provider is registered before any other code tries to use it. This should resolve the "package org.bouncycastle.crypto.tls does not exist" error.