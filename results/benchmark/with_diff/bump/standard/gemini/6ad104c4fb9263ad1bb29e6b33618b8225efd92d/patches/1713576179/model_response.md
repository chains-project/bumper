```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder {

    private final TlsFatalAlert alert;

    public ChachaDecoder(TlsFatalAlert alert) {
        this.alert = alert;
    }

    public void decode(byte[] in, int inOff, int len) throws IOException {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int key_len = in[inOff];
        int iv_len = in[inOff + 1];

        if (key_len < 0 || key_len > 255 || iv_len < 0 || iv_len > 255 || len < 16 + key_len + iv_len) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] key = new byte[key_len];
        byte[] iv = new byte[iv_len];

        System.arraycopy(in, inOff + 2, key, 0, key_len);
        System.arraycopy(in, inOff + 2 + key_len, iv, 0, iv_len);

        // TODO: Implement ChaCha20 decryption
    }
}
```