```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private static final int CHACHA20_KEY_SIZE = 32;
    private static final int CHACHA20_NONCE_SIZE = 12;

    private final ByteBuffer buffer;
    private final byte[] key;
    private final byte[] nonce;

    public ChachaDecoder(ByteBuffer buffer, byte[] key, byte[] nonce) {
        this.buffer = buffer;
        this.key = key;
        this.nonce = nonce;
    }

    public void decode(ByteBuffer output) throws IOException {
        if (buffer.remaining() < CHACHA20_KEY_SIZE + CHACHA20_NONCE_SIZE) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] key = new byte[CHACHA20_KEY_SIZE];
        buffer.get(key);

        byte[] nonce = new byte[CHACHA20_NONCE_SIZE];
        buffer.get(nonce);

        byte[] ciphertext = new byte[buffer.remaining()];
        buffer.get(ciphertext);

        Chacha20.decrypt(key, nonce, ciphertext, ciphertext, 0, ciphertext.length);

        output.put(ciphertext);
    }

    public static void main(String[] args) throws IOException {
        // Test code
        byte[] key = new byte[CHACHA20_KEY_SIZE];
        byte[] nonce = new byte[CHACHA20_NONCE_SIZE];
        byte[] ciphertext = new byte[1024];

        ByteBuffer buffer = ByteBuffer.allocate(CHACHA20_KEY_SIZE + CHACHA20_NONCE_SIZE + ciphertext.length);
        buffer.put(key);
        buffer.put(nonce);
        buffer.put(ciphertext);

        ByteBuffer output = ByteBuffer.allocate(ciphertext.length);
        ChachaDecoder decoder = new ChachaDecoder(buffer, key, nonce);
        decoder.decode(output);

        System.out.println(output.array());
    }
}
```