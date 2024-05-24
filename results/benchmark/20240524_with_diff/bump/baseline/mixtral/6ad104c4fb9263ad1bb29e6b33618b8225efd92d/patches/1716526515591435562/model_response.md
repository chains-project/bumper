Here's the proposed patch for the `ChachaDecoder.java` file:

```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

// ...

@Override
public void onDecryptError(ChannelHandlerContext ctx, Throwable cause) {
    if (cause instanceof TlsFatalAlert) {
        TlsFatalAlert fatalAlert = (TlsFatalAlert) cause;
        AlertDescription alertDescription = fatalAlert.getAlertDescription();
        LOGGER.warn("Decryption error: {}", alertDescription);
    } else {
        LOGGER.warn("Decryption error: {}", cause.getMessage());
    }
    ctx.fireExceptionCaught(cause);
}
```

This patch adds the import for the new `TlsFatalAlert` class and updates the `if` statement to check for `TlsFatalAlert`. It also adds the necessary cast to `TlsFatalAlert` and calls the new method `getAlertDescription()` on it.