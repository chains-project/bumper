```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLSocketFactory;

import io.github.hapjava.server.impl.crypto.ChachaDecoder;

public class ChachaDecoder {
    public ChachaDecoder() {
        String providerName = "BC";
        Provider bcProvider = Security.getProvider(providerName);
        if (bcProvider == null) {
            try {
                bcProvider = (Provider) Class.forName("org.bouncycastle.jce.provider.BouncyCastleProvider").newInstance();
                Security.addProvider(bcProvider);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }
}
```