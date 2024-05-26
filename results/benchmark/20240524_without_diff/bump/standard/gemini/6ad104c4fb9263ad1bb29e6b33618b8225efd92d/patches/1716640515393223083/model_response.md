```java
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;
import java.net.Socket;
import java.nio.ByteBuffer;
import java.util.Arrays;

public class ChachaDecoder {

    private final Socket socket;
    private final byte[] key;
    private final byte[] nonce;
    private final int counter;

    public ChachaDecoder(Socket socket, byte[] key, byte[] nonce, int counter) {
        this.socket = socket;
        this.key = key;
        this.nonce = nonce;
        this.counter = counter;
    }

    public byte[] decode(byte[] data) throws IOException {
        ByteBuffer buffer = ByteBuffer.allocate(data.length + 8);
        buffer.put(data);
        buffer.putInt(counter);
        buffer.flip();

        byte[] encrypted = new byte[buffer.remaining()];
        buffer.get(encrypted);

        byte[] decrypted = ChaCha.decrypt(encrypted, key, nonce, counter);

        // Check for padding
        int paddingLength = decrypted[decrypted.length - 1];
        if (paddingLength > decrypted.length || paddingLength < 0) {
            throw new IOException("Invalid padding length");
        }

        // Check for AlertDescription
        if (decrypted.length >= 2 && decrypted[0] == AlertDescription.close_notify) {
            throw new IOException("AlertDescription: " + decrypted[1]);
        }

        return Arrays.copyOf(decrypted, decrypted.length - paddingLength);
    }
}
```