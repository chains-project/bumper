Here's a possible patch to fix the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public static TlsFatalAlert getTlsFatalAlert(short alert) {
        return TlsFatalAlert.getInstance(alert);
    }
}
```
The patch removes the `AlertDescription` import and uses the `TlsFatalAlert` class from the updated library version to create an instance of `TlsFatalAlert` with the given `alert` value.
The `getAlertDescription()` method is not needed, as the `TlsFatalAlert` instance returned by `getInstance()` already contains the necessary information.

Note that this patch assumes that the `ChachaDecoder` class is not modified in the new library version, and that the `TlsFatalAlert` class has the same functionality and constructor in the new version.