Here's the proposed patch for the failing client code:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    // ...

    @Override
    public void onTlsFatalAlertReceived(short alertDescription) {
        AlertDescription description = TlsFatalAlert.getAlertDescription(alertDescription);
        // ...
    }

    // ...
}
```

This patch changes the way the `AlertDescription` is obtained from the `alertDescription` short value. Instead of using the deprecated constructor, it now uses the new static method `TlsFatalAlert.getAlertDescription(alertDescription)` to get the corresponding `AlertDescription` value.