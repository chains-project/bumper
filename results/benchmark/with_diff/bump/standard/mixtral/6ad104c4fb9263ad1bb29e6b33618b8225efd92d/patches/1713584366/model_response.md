Here's the proposed patch for the failing method. I added a new variable `alertDescription` of type `AlertDescription` to replace the removed method `TlsFatalAlert.getAlertDescription()`.

```java
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;

public class ChachaDecoder {
    // ...

    private void decode(TlsContext context, InputStream input) throws IOException {
        // ...

        try {
            // ...

            short alertDescriptionValue = input.readShort();
            AlertDescription alertDescription = AlertDescription.forValue(alertDescriptionValue);

            throw new TlsFatalAlert(alertDescription);
        } catch (TlsFatalAlert ex) {
            // ...
        }
    }

    // ...
}
```