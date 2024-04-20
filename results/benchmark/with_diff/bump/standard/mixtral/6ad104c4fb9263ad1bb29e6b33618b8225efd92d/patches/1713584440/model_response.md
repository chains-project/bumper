Here's the proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.TlsAlert;

// ...

public class ChachaDecoder {

    // ...

    private void decodeAlert(TlsContext context, InputStream input) throws TlsFatalAlert {
        int alertLevel = input.read();
        int alertDescription = input.read();
        TlsAlert alert = new TlsAlert(alertLevel, AlertDescription.getAlertDescription(alertDescription));
        // ...
    }

    // ...

}
```

The patch uses the new class `TlsAlert` and the new method `AlertDescription.getAlertDescription(alertDescription)` from the updated library. I've also imported the `TlsAlert` class to make the code more readable.