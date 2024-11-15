```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.ReadableByteChannel;

public class ChachaDecoder {

    private final ReadableByteChannel channel;
    private final int nonceLength;

    public ChachaDecoder(ReadableByteChannel channel, int nonceLength) {
        this.channel = channel;
        this.nonceLength = nonceLength;
    }

    public ByteBuffer decode(ByteBuffer buffer) throws IOException {
        if (buffer.remaining() < nonceLength) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] nonce = new byte[nonceLength];
        channel.read(ByteBuffer.wrap(nonce));

        // TODO: Decrypt the buffer using the nonce
        // Use the ChaCha20Poly1305 cipher from Bouncy Castle
        // See https://www.bouncycastle.org/docs/pkixdocs1.5on/org/bouncycastle/crypto/tls/ChaCha20Poly1305.html

        return buffer;
    }
}
```