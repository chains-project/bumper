Here's a proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.security.Security;

public class ChachaDecoder {
    // ...

    static {
        Security.addProvider(new BouncyCastleProvider());
    }

    // ...
}
```
This patch adds a static block to the `ChachaDecoder` class that initializes the Bouncy Castle provider. This ensures that the required classes from the `org.bouncycastle.crypto.tls` package are available at runtime.

Note: This patch assumes that the Bouncy Castle library (`bcpkix-jdk15on` and `bcprov-jdk15on`) is added as a dependency in the project's build system. If not, you need to add it first. You can find more information on how to add it in the project's documentation.