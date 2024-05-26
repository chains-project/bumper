```java
import java.security.Provider;
import java.security.Security;
import org.bouncycastle.jce.provider.BouncyCastleProvider;

public class ChachaDecoder {
    static {
        Provider bcProvider = new org.bouncycastle.jce.provider.BouncyCastleProvider();
        Security.addProvider(bcProvider);
    }
    // rest of the class
}
```