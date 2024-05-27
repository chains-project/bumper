```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public TlsFatalAlert decode(byte[] data) {
        return new TlsFatalAlert(TlsFatalAlert.BAD_CERTIFICATE, "Invalid ChaCha20Poly1305 cipher suite");
    }
}
```