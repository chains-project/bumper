```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] data, int offset, int len) throws TlsFatalAlert {
        // TODO: Implement the Chacha20Poly1305 decoder using the new Bouncy Castle API.
        // You can use the following methods from the new API:
        // - TlsFatalAlert.getAlertDescription()
        // - TlsFatalAlert(short)

        // Note that the old methods TlsFatalAlert.getAlertDescription() and TlsFatalAlert(short)
        // have been removed in the new Bouncy Castle version.

        // You can also use any other methods from the Bouncy Castle API that are available in the new version.
    }
}
```