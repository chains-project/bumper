Here's the proposed patch for the `ChachaDecoder.java` file:

```java
import org.bouncycastle.crypto.tls.TlsAlert;

// ...

private void handleError(short errorCode) {
    TlsAlert alert = new TlsAlert(errorCode);
    AlertDescription desc = alert.getAlertDescription();
    // ...
}
```

The patch replaces the usage of `TlsFatalAlert` with the new `TlsAlert` class and updates the method for getting the `AlertDescription`.