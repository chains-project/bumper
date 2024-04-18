```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.io.OutputStream;

public class ChachaDecoder extends TlsCipher {

    private static final int CHACHA_KEY_SIZE = 32;
    private static final int CHACHA_IV_SIZE = 12;

    private final TlsContext context;
    private final OutputStream output;

    private byte[] key;
    private byte[] iv;

    public ChachaDecoder(TlsContext context, OutputStream output) {
        this.context = context;
        this.output = output;
    }

    @Override
    public void init(TlsContext context, int encryptionMode) throws IOException {
        this.key = context.getSecurityParameters().getMasterSecret();
        this.iv = context.getSecurityParameters().getClientRandom();

        if (encryptionMode != TlsCipher.DECRYPTION_MODE) {
            throw new IOException("ChachaDecoder can only be used for decryption");
        }
    }

    @Override
    public byte[] decodeCiphertext(long seqNo, byte[] ciphertext, int offset, int len) throws IOException {
        byte[] plaintext = new byte[len];

        chacha20(key, iv, seqNo, ciphertext, offset, len, plaintext, 0);

        return plaintext;
    }

    private static void chacha20(byte[] key, byte[] iv, long seqNo, byte[] ciphertext, int offset, int len, byte[] plaintext, int outOffset) {
        // TODO: Implement ChaCha20
    }
}
```