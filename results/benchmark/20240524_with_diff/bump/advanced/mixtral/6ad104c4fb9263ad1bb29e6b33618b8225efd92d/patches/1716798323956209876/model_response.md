Here's the proposed patch for the failing client code:
```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void processAlert(short alertCode) {
    AlertDescription alertDescription = TlsFatalAlert.getAlertDescription(alertCode);
    // ...
}
```
The patch adds an import statement for the new `TlsFatalAlert` class and uses the new method `getAlertDescription` to get the `AlertDescription`.