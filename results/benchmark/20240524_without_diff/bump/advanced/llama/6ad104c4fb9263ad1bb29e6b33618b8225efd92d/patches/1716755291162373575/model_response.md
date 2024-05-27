```java
import java.security.Security;
import javax.net.ssl.SSLException;

public class ChachaDecoder {
    public void decode() throws SSLException {
        Security.removeProvider("BC");
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
    }
}
```