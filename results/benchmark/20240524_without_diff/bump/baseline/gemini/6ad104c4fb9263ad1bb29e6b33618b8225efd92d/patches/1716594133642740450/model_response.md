```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final TlsCipher cipher;

    public ChachaDecoder(TlsCipher cipher) {
        this.cipher = cipher;
    }

    public byte[] decode(byte[] input, int offset, int len) throws IOException {
        // Check if the input is large enough to contain the record header.
        if (len < TlsProtocol.RECORD_HEADER_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Extract the record header.
        ByteBuffer header = ByteBuffer.wrap(input, offset, TlsProtocol.RECORD_HEADER_LENGTH);
        int type = header.get() & 0xff;
        int version = header.getShort() & 0xffff;
        int length = header.getShort() & 0xffff;

        // Check if the record length is valid.
        if (length < 0 || length > TlsProtocol.MAX_FRAGMENT_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Check if the input is large enough to contain the entire record.
        if (len < TlsProtocol.RECORD_HEADER_LENGTH + length) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Decrypt the record body.
        byte[] body = cipher.decodeCiphertext(input, offset + TlsProtocol.RECORD_HEADER_LENGTH, length);

        // Check if the record body is valid.
        if (body == null) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Return the decrypted record body.
        return body;
    }
}
```