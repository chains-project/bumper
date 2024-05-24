Here's a possible patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.TlsFatalAlertReason;

public class ChachaDecoder {
    // ...

    @Override
    public void onTlsFatalAlertReceived(short alertDescription) {
        TlsFatalAlertReason reason = TlsFatalAlertReason.get(alertDescription);
        // ...
    }

    // ...
}
```

This patch removes the direct use of the `TlsFatalAlert` constructor, which has been removed in the new library version. Instead, it uses the `TlsFatalAlertReason` enum, which has been added in the new version. The `getAlertDescription()` method has also been removed, so it has been replaced with a call to `TlsFatalAlertReason.get(alertDescription)` to get the corresponding `TlsFatalAlertReason` value.