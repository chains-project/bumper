Here's the patched method:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.security.GeneralSecurityException;
import java.security.NoSuchAlgorithmException;

public class ChachaDecoder {
    // ...

    private TlsFatalAlert createAlert(int alertDescription) throws GeneralSecurityException {
        try {
            return new TlsFatalAlert(alertDescription);
        } catch (NoSuchAlgorithmException e) {
            throw new GeneralSecurityException("Failed to create TlsFatalAlert", e);
        }
    }

    // ...
}
```
To fix the issue, I added a try-catch block around the creation of the `TlsFatalAlert` object to handle the `NoSuchAlgorithmException`. This way, the code can continue executing even if the external dependency is not available.