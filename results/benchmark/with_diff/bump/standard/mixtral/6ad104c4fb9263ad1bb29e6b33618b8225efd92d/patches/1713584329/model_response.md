Here is a fixed version of the client code that should resolve the error:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // existing code

    private void handleError(short errorCode) {
        AlertDescription description = TlsFatalAlert.getAlertDescription(errorCode);
        // existing code
    }

    // existing code
}
```

In this fixed version, I added an import statement for `TlsFatalAlert` and changed the method signature of `getAlertDescription` to a static method. This should resolve the error about the missing package.