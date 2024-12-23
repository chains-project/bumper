```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsUtils;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final int cipherState;

    public ChachaDecoder(int cipherState) {
        this.cipherState = cipherState;
    }

    public byte[] decode(byte[] in, int inOff, int len) throws IOException {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextLength = len - 16;
        byte[] plaintext = new byte[plaintextLength];

        ByteBuffer buffer = ByteBuffer.wrap(in, inOff, len);
        byte[] nonce = new byte[12];
        buffer.get(nonce);
        byte[] key = new byte[32];
        buffer.get(key);
        TlsUtils.chacha20(key, nonce, buffer.array(), buffer.arrayOffset() + 16, plaintext, 0, plaintextLength);

        return plaintext;
    }

    public byte[] decodeCiphertext(byte[] in, int inOff, int len) throws IOException {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextLength = len - 16;
        byte[] plaintext = new byte[plaintextLength];

        ByteBuffer buffer = ByteBuffer.wrap(in, inOff, len);
        byte[] nonce = new byte[12];
        buffer.get(nonce);
        byte[] key = new byte[32];
        buffer.get(key);
        TlsUtils.chacha20(key, nonce, buffer.array(), buffer.arrayOffset() + 16, plaintext, 0, plaintextLength);

        return plaintext;
    }

    public int getCipherState() {
        return cipherState;
    }
}
```