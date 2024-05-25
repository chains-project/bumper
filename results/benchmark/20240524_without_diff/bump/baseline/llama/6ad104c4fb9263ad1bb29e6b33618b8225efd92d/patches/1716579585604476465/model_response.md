```java
import java.security.Security;

public class ChachaDecoder {
    static {
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
    }
}
```