```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] data, int offset, int len) {
        if (data == null) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }
        if (offset < 0 || len < 0 || offset + len > data.length) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }
        // TODO: Implement ChaCha20 decryption
    }
}
```