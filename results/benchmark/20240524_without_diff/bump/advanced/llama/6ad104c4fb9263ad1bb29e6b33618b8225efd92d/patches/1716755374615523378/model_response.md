```java
import java.security.Provider;
import java.security.Security;

import javax.net.ssl.SSLContext;
import javax.net.ssl.SSLException;

import java.io.IOException;

public class ChachaDecoder {
    public void decode() throws IOException, SSLException {
        Provider bcProvider = Security.getProvider("BC");
        if (bcProvider == null) {
            Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        }
    }
}
```