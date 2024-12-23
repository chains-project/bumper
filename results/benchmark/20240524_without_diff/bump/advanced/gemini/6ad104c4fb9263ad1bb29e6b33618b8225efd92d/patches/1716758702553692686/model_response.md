```java
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.nio.channels.ReadableByteChannel;

public class ChachaDecoder {

    private final ByteBuffer buffer;
    private final int keyLength;
    private final int ivLength;

    public ChachaDecoder(int keyLength, int ivLength) {
        this.buffer = ByteBuffer.allocate(keyLength + ivLength);
        this.keyLength = keyLength;
        this.ivLength = ivLength;
    }

    public void decode(ReadableByteChannel channel, ByteBuffer output) throws IOException {
        if (buffer.remaining() > 0) {
            channel.read(buffer);
            if (buffer.remaining() > 0) {
                throw new AlertDescription(AlertDescription.handshake_failure);
            }
        }

        byte[] key = new byte[keyLength];
        byte[] iv = new byte[ivLength];
        buffer.flip();
        buffer.get(key);
        buffer.get(iv);
        buffer.clear();

        output.position(output.position() + keyLength + ivLength);
    }
}
```