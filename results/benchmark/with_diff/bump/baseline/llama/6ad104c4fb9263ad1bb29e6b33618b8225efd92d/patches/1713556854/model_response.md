Here's a possible patch to fix the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public static TlsFatalAlert getTlsFatalAlert(short alert) {
        return TlsFatalAlert.getInstance(alert);
    }
}
```
The patch removes the reference to `AlertDescription` and instead uses the `TlsFatalAlert` class directly. The `getInstance` method is used to create a new instance of `TlsFatalAlert` with the given `alert` value.

This patch should fix the error caused by the missing `AlertDescription` class and allow the client code to compile and run successfully.