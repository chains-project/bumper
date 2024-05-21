```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

/**
 * A ChaCha20Poly1305 decoder.
 */
public class ChachaDecoder {

    private final TlsProtocol protocol;
    private final ByteBuffer buffer;

    /**
     * Creates a new ChaCha20Poly1305 decoder.
     *
     * @param protocol the TLS protocol
     * @param buffer   the buffer to decode
     */
    public ChachaDecoder(TlsProtocol protocol, ByteBuffer buffer) {
        this.protocol = protocol;
        this.buffer = buffer;
    }

    /**
     * Decodes the next message.
     *
     * @return the decoded message
     * @throws IOException if an error occurs
     */
    public byte[] decode() throws IOException {
        int length = buffer.getInt();
        if (length < 0 || length > protocol.getMaxFragmentLength()) {
            throw new IOException("Invalid message length: " + length);
        }

        byte[] data = new byte[length];
        buffer.get(data);

        byte[] mac = new byte[16];
        buffer.get(mac);

        // TODO: Verify the MAC

        return data;
    }
}
```