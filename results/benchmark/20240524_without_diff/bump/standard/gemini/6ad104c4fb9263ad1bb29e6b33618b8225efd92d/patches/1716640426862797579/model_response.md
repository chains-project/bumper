```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private static final int NONCE_LENGTH = 12;
    private static final int TAG_LENGTH = 16;

    private final TlsCipher cipher;
    private final TlsContext context;
    private final ByteBuffer buffer;

    public ChachaDecoder(TlsCipher cipher, TlsContext context) {
        this.cipher = cipher;
        this.context = context;
        this.buffer = ByteBuffer.allocate(cipher.getCiphertextDecodeLimit(NONCE_LENGTH + TAG_LENGTH));
    }

    public byte[] decode(byte[] input, int offset, int len) throws IOException {
        if (len < NONCE_LENGTH + TAG_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        buffer.clear();
        buffer.put(input, offset, len);
        buffer.flip();

        byte[] nonce = new byte[NONCE_LENGTH];
        buffer.get(nonce);

        byte[] tag = new byte[TAG_LENGTH];
        buffer.get(tag);

        byte[] plaintext = new byte[buffer.remaining()];
        buffer.get(plaintext);

        if (!cipher.verifyRecord(context, nonce, plaintext, 0, plaintext.length, tag)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }
}
```