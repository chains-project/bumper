```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private static final int CHACHA_KEY_SIZE = 32;
    private static final int CHACHA_NONCE_SIZE = 12;
    private static final int CHACHA_POLY1305_TAG_SIZE = 16;

    private final TlsContext context;
    private final byte[] key;
    private final byte[] nonce;

    public ChachaDecoder(TlsContext context, byte[] key, byte[] nonce) {
        this.context = context;
        this.key = key;
        this.nonce = nonce;
    }

    public byte[] decode(byte[] input, int offset, int len) throws IOException {
        if (len < CHACHA_POLY1305_TAG_SIZE) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] tag = new byte[CHACHA_POLY1305_TAG_SIZE];
        System.arraycopy(input, offset + len - CHACHA_POLY1305_TAG_SIZE, tag, 0, CHACHA_POLY1305_TAG_SIZE);

        byte[] plaintext = new byte[len - CHACHA_POLY1305_TAG_SIZE];
        System.arraycopy(input, offset, plaintext, 0, len - CHACHA_POLY1305_TAG_SIZE);

        //++
        if (!context.getCrypto().verify_data(key, nonce, 0, plaintext, 0, plaintext.length, tag)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }
}
```