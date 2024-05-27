Here's the proposed patch for the client code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.tls.TlsFatalAlert;

public class ChachaDecoder {
    // ...

    private void handleAlert(short alertDescription) {
        AlertDescription description = AlertDescription.getAlertDescription(alertDescription);
        if (description == AlertDescription.internal_error) {
            throw new TlsFatalAlert(TlsFatalAlert.INTERNAL_ERROR);
        }
        // ...
    }
}
```

The patch introduces the new class `TlsFatalAlert` from the `org.bouncycastle.tls` package and uses it to replace the removed constructor. The `AlertDescription` class is still used to get the alert description.