Here is a patched version of the failing method that uses the Bouncy Castle library's new class `TlsFatalAlert` constructor:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.AlertDescription;

// ...

private void sendFatalAlert(short alertDescription) {
    AlertDescription description = AlertDescription.valueOf(alertDescription);
    throw new TlsFatalAlert(description);
}
```
This new version uses the new constructor `TlsFatalAlert(AlertDescription)` to create a `TlsFatalAlert` instance. The `AlertDescription` enum is used to get the alert description corresponding to the given short value.

Note that the `TlsFatalAlert` constructor that takes a short argument has been removed in the new library version, so it can no longer be used.