```java
import java.security.Provider;
import java.security.Security;

public class ChachaDecoder {
    public ChachaDecoder() {
        Provider bcProvider = new org.bouncycastle.jce.provider.BouncyCastleProvider();
        Security.addProvider(bcProvider);
    }
}
```