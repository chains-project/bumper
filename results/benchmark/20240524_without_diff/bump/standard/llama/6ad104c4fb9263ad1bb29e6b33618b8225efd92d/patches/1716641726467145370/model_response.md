```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

public class ChachaDecoder {
    public ChachaDecoder() {
        String tlsProviderName = "Conscrypt";
        Provider tlsProvider = Security.getProvider(tlsProviderName);
        if (tlsProvider == null) {
            tlsProvider = new org.conscrypt.OpenSSLProvider(tlsProviderName);
            Security.addProvider(tlsProvider);
        }
    }
}
```