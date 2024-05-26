```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsUtils;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.ByteArrayInputStream;
import java.io.IOException;
import java.security.GeneralSecurityException;

/**
 * A ChaCha20Poly1305 cipher for TLS 1.3.
 */
public class ChachaDecoder extends AbstractTlsCipher {

    private static final int CHACHA20_POLY1305_KEY_SIZE = 32;
    private static final int CHACHA20_POLY1305_IV_SIZE = 12;
    private static final int CHACHA20_POLY1305_TAG_SIZE = 16;

    private final Cipher cipher;
    private final TlsContext context;
    private final SecretKeySpec key;
    private final IvParameterSpec iv;

    public ChachaDecoder(TlsContext context, SecretKeySpec key, IvParameterSpec iv) throws IOException {
        super(context);
        this.context = context;
        this.key = key;
        this.iv = iv;

        try {
            this.cipher = TlsUtils.getCipher("ChaCha20/Poly1305");
        } catch (GeneralSecurityException e) {
            throw new IOException("Failed to initialize ChaCha20/Poly1305 cipher", e);
        }
    }

    @Override
    public int getPlaintextLimit(int ciphertextLimit) {
        return ciphertextLimit - CHACHA20_POLY1305_TAG_SIZE;
    }

    @Override
    public byte[] decodeCiphertext(int seqNo, byte[] ciphertext, int offset, int len) throws IOException {
        if (len < CHACHA20_POLY1305_TAG_SIZE) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        try {
            cipher.init(Cipher.DECRYPT_MODE, key, iv);
            byte[] plaintext = cipher.doFinal(ciphertext, offset, len - CHACHA20_POLY1305_TAG_SIZE);
            byte[] tag = cipher.doFinal(new ByteArrayInputStream(plaintext), len - CHACHA20_POLY1305_TAG_SIZE, CHACHA20_POLY1305_TAG_SIZE);
            if (!TlsUtils.constantTimeAreEqual(tag, ciphertext, offset + len - CHACHA20_POLY1305_TAG_SIZE)) {
                throw new TlsFatalAlert(AlertDescription.bad_record_mac);
            }
            return plaintext;
        } catch (GeneralSecurityException e) {
            throw new TlsFatalAlert(AlertDescription.internal_error, e);
        }
    }
}
```