Here's the proposed patch for the `ChachaDecoder.java` file:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

@Override
public void notifyCloseAlertReceived(short alertDescription) {
    if (alertDescription == AlertDescription.close_notify) {
        return;
    }
    throw new TlsFatalAlert(alertDescription);
}
```

The changes include importing the new `TlsFatalAlert` class from the updated library and using it to replace the removed `TlsFatalAlert` constructor.