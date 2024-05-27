```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.net.Socket;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final Socket socket;
    private final ByteBuffer buffer;

    public ChachaDecoder(Socket socket, ByteBuffer buffer) {
        this.socket = socket;
        this.buffer = buffer;
    }

    public byte[] decode(byte[] data) throws IOException {
        int length = data.length;
        if (length < TlsProtocol.RECORD_HEADER_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int headerLength = data[0] & 0xFF;
        if (headerLength < TlsProtocol.RECORD_HEADER_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        if (length < headerLength) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int payloadLength = length - headerLength;
        byte[] payload = new byte[payloadLength];
        System.arraycopy(data, headerLength, payload, 0, payloadLength);

        return payload;
    }
}
```