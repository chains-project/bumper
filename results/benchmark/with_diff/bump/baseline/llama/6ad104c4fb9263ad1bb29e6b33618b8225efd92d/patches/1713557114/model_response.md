Here's a proposed patch to fix the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public static TlsFatalAlert getTlsFatalAlert(short alertDescription) {
        return TlsFatalAlert.getInstance(alertDescription);
    }
}
```
Explanation:

The failing code imports `AlertDescription` from `org.bouncycastle.crypto.tls`, which no longer exists in the new library version. We replace the import with `TlsFatalAlert` from the same package, which has an identical constructor and can be used in the same way.

The `getAlertDescription()` method is removed in the new library version, so we replace the call with `TlsFatalAlert.getInstance(alertDescription)`, which achieves the same result.

No other changes are needed in the code, as the rest of the code is not affected by the library changes.