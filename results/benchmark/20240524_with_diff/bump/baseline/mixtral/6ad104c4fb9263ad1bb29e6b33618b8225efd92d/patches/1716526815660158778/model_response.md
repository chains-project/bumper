Here's the proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // ...

    @Override
    protected void decode(InputStream input, byte[] data) throws IOException {
        // ...

        short alertDescription = input.readShort();
        if (alertDescription == TlsFatalAlert.BAD_RECORD_MAC) {
            throw new TlsFatalAlert(TlsFatalAlert.BAD_RECORD_MAC, AlertDescription.decode(alertDescription));
        }

        // ...
    }
}
```

The patch introduces a new import statement for the `TlsFatalAlert` class and modifies the `decode` method to use the new constructor for `TlsFatalAlert`. The `getAlertDescription` method has been removed in the new version, so it is not used in this patch.