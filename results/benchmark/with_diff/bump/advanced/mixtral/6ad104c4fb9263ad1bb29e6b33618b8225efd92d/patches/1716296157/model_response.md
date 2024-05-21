Here is the proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // existing code...

    private void handleError(short errorCode) {
        AlertDescription description = TlsFatalAlert.getAlertDescription(errorCode);
        // existing code...
    }

    // existing code...
}
```

Note that I added a new import statement for `org.bouncycastle.crypto.tls.TlsFatalAlert`, and modified the `handleError` method to use the new `TlsFatalAlert.getAlertDescription` method instead of the removed constructor.