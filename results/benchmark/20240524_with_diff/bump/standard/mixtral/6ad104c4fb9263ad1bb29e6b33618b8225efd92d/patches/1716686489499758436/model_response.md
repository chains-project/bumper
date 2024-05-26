Here's a patch that you can apply to the failing client code:
```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsFatalAlert.AlertDescription;

// ...

private void decode(ByteBuffer byteBuffer) {
  // ...

  try {
    // Use the new method to get the AlertDescription
    AlertDescription alertDescription = TlsFatalAlert.getAlertDescription(byteBuffer.getShort());

    // ...
  } catch (TlsFatalAlert ex) {
    // Handle the exception
  }

  // ...
}
```
In this patch, I've imported the new classes `TlsFatalAlert` and `AlertDescription` that were added in the new library version.
Instead of using the constructor `TlsFatalAlert(short)` which was removed, I use the new method `TlsFatalAlert.getAlertDescription(short)` to get the `AlertDescription` from the `short` value.
This way, the code should work with the new library version.