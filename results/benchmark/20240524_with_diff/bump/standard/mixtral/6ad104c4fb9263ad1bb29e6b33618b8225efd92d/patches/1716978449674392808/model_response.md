Here's the fixed failing method. I've imported the new classes from the updated library version:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

private void handleError(short errorCode) {
    AlertDescription description = TlsFatalAlert.getAlertDescription(errorCode);
    // ...
}
```

In this patch, I imported the `TlsFatalAlert` class and used the new method `getAlertDescription` to replace the removed constructor.