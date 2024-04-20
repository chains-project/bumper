Here is a fixed version of the client code that should resolve the error:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // existing code

    private void handleError(short alertDescription) {
        AlertDescription description = TlsFatalAlert.getAlertDescription(alertDescription);
        // existing code
    }
}
```

The fix involves importing the new `TlsFatalAlert` class and using its `getAlertDescription` method to obtain the `AlertDescription` object. This method was added in the new library version and can be used to replace the removed constructor.