Here's the fixed failing method with the necessary changes:

```java
import org.bouncycastle.crypto.tls.TlsAlert;

// ...

private void handleInvalidRecordType(TlsUtils.TlsHandshakeType handshakeType, byte[] record) throws TlsFatalAlert {
    short alertDescription = AlertDescription.unexpected_message.getNumber();
    throw new TlsFatalAlert(alertDescription);
}
```

The changes include importing `org.bouncycastle.crypto.tls.TlsAlert` instead of `org.bouncycastle.crypto.tls.AlertDescription`, and using `TlsAlert` with the `getNumber()` method to get the alert description number. The `TlsFatalAlert` constructor has also changed to accept a `short` instead of the `AlertDescription` enum.