```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final int keyLength;
    private final int nonceLength;

    public ChachaDecoder(int keyLength, int nonceLength) {
        this.keyLength = keyLength;
        this.nonceLength = nonceLength;
    }

    public byte[] decode(byte[] ciphertext, byte[] key, byte[] nonce) throws IOException {
        if (ciphertext.length < nonceLength) {
            throw new TlsFatalAlert(TlsProtocol.ALERT_DECODE_ERROR);
        }

        ByteBuffer buffer = ByteBuffer.allocate(ciphertext.length - nonceLength);
        buffer.put(ciphertext, nonceLength, ciphertext.length - nonceLength);
        buffer.flip();

        byte[] plaintext = new byte[buffer.remaining()];
        buffer.get(plaintext);

        return plaintext;
    }
}
```