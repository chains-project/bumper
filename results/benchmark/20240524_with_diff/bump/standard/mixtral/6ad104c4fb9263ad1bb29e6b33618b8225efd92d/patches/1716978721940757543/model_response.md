Here's the proposed patch for the `ChachaDecoder.java` file:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void handleError(short errorCode) {
    AlertDescription description = TlsFatalAlert.getAlertDescription(errorCode);
    // ...
}
```

The patch adds an import statement for `TlsFatalAlert` and uses the new method `TlsFatalAlert.getAlertDescription(short)` to get the `AlertDescription`.