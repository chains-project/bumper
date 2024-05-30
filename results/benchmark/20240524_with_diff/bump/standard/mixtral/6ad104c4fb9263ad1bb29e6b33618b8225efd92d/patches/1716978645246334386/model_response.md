Here's the patched version of the failing method in `ChachaDecoder.java`. I've introduced a new variable `alertDescription` to replace the direct usage of `TlsFatalAlert` constructor and method.

```java
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;

public class ChachaDecoder {
    // ...

    private void decode(TlsContext context, InputStream input) throws IOException {
        // ...

        if (type == TlsConstants.ContentType.alert) {
            int alertDescriptionCode = input.read();
            AlertDescription alertDescription = AlertDescription.get(alertDescriptionCode);
            throw new TlsFatalAlert(alertDescription);
        }

        // ...
    }

    // ...
}
```

The patch introduces a new variable `alertDescription` that gets the `AlertDescription` based on the `alertDescriptionCode` instead of using the deprecated constructor `TlsFatalAlert(short)`. The `getAlertDescription()` method has not been deprecated, so it can still be used.