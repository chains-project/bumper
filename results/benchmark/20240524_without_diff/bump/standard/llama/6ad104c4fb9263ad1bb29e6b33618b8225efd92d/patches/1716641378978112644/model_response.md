```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

public class ChachaDecoder {
    public ChachaDecoder() {
        String providerName = "BC";
        Provider bcProvider = Security.getProvider(providerName);
        if (bcProvider == null) {
            try {
                Class<?> bcClass = Class.forName("org.bouncycastle.jce.provider.BouncyCastleProvider");
                bcProvider = (Provider) bcClass.newInstance();
                Security.addProvider(bcProvider);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }
}
```