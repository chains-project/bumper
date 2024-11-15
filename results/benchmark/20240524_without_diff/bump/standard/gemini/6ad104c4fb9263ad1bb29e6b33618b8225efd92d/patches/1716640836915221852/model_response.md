```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.io.InputStream;
import java.nio.ByteBuffer;

/**
 * A ChaCha decoder for TLS.
 */
public class ChachaDecoder extends InputStream {

    private final InputStream input;
    private final ByteBuffer buffer;

    /**
     * Constructs a new ChaCha decoder.
     *
     * @param input the input stream to decode.
     * @param buffer the buffer to use for decoding.
     */
    public ChachaDecoder(InputStream input, ByteBuffer buffer) {
        this.input = input;
        this.buffer = buffer;
    }

    @Override
    public int read() throws IOException {
        if (!buffer.hasRemaining()) {
            readBlock();
        }
        return buffer.get() & 0xFF;
    }

    private void readBlock() throws IOException {
        int length = input.read(buffer.array(), buffer.position(), buffer.remaining());
        if (length < 0) {
            throw new TlsFatalAlert(TlsProtocol.ALERT_DECRYPT_ERROR);
        }
        buffer.position(buffer.position() + length);
    }
}
```