```java
import java.security.Provider;
import java.security.Security;
import javax.net.ssl.SSLException;

public class ChachaDecoder {
    public void decode() throws SSLException {
        Provider bcProvider = Security.getProvider("BC");
        if (bcProvider != null) {
            // No operation
        } else {
            Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        }
    }
}
```