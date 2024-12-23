```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private static final short MAX_KEY_LENGTH = 255;
    private static final short MAX_IV_LENGTH = 12;

    private final TlsFatalAlert fatalAlert;

    public ChachaDecoder(TlsFatalAlert fatalAlert) {
        this.fatalAlert = fatalAlert;
    }

    public byte[] decode(byte[] in, int inOff, int len) throws IOException {
        if (len < MAX_KEY_LENGTH + MAX_IV_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] key = new byte[MAX_KEY_LENGTH];
        System.arraycopy(in, inOff, key, 0, MAX_KEY_LENGTH);
        inOff += MAX_KEY_LENGTH;

        byte[] iv = new byte[MAX_IV_LENGTH];
        System.arraycopy(in, inOff, iv, 0, MAX_IV_LENGTH);
        inOff += MAX_IV_LENGTH;

        ByteBuffer buffer = ByteBuffer.allocate(len - MAX_KEY_LENGTH - MAX_IV_LENGTH);
        buffer.put(in, inOff, len - MAX_KEY_LENGTH - MAX_IV_LENGTH);
        buffer.flip();

        // TODO: Implement ChaCha20 decryption using the provided key and IV.

        return buffer.array();
    }
}
```