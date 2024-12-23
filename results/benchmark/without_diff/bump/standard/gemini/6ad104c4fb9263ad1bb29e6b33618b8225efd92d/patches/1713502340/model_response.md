```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsCompression;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsCredentials;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsUtils;

import java.io.IOException;
import java.io.OutputStream;

/**
 * A ChaCha20Poly1305 cipher that uses the TLS API.
 */
public class ChachaDecoder implements TlsCipher {

    private static final int CHACHA20_POLY1305_KEY_SIZE = 32;
    private static final int CHACHA20_POLY1305_IV_SIZE = 12;
    private static final int CHACHA20_POLY1305_TAG_SIZE = 16;

    private TlsContext context;
    private TlsCredentials credentials;
    private OutputStream output;

    private byte[] key;
    private byte[] iv;

    /**
     * Creates a new ChaCha20Poly1305 cipher.
     *
     * @param context    the TLS context
     * @param credentials the TLS credentials
     * @param output     the output stream
     */
    public ChachaDecoder(TlsContext context, TlsCredentials credentials, OutputStream output) {
        this.context = context;
        this.credentials = credentials;
        this.output = output;
    }

    /**
     * Initializes the cipher.
     *
     * @param isServer  whether this is the server
     * @param encrypting whether this is encrypting
     * @throws IOException if an error occurs
     */
    public void init(TlsContext context, boolean isServer, boolean encrypting) throws IOException {
        this.context = context;

        if (encrypting) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }

        // Get the key and IV from the TLS context.
        key = context.getSecurityParameters().getMasterSecret();
        iv = context.getSecurityParameters().getServerRandom();

        // Check the key and IV sizes.
        if (key.length != CHACHA20_POLY1305_KEY_SIZE) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }
        if (iv.length != CHACHA20_POLY1305_IV_SIZE) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }
    }

    /**
     * Gets the cipher key size.
     *
     * @return the cipher key size
     */
    public int getCipherKeySize() {
        return CHACHA20_POLY1305_KEY_SIZE;
    }

    /**
     * Gets the cipher algorithm name.
     *
     * @return the cipher algorithm name
     */
    public String getAlgorithmName() {
        return "ChaCha20Poly1305";
    }

    /**
     * Gets the cipher block size.
     *
     * @return the cipher block size
     */
    public int getBlockSize() {
        return 1;
    }

    /**
     * Gets the cipher implementation.
     *
     * @return the cipher implementation
     */
    public TlsCipher getImplementation() {
        return this;
    }

    /**
     * Encrypts the given data.
     *
     * @param input  the input data
     * @param offset the input offset
     * @param length the input length
     * @return the encrypted data
     * @throws IOException if an error occurs
     */
    public byte[] encodePlaintext(long seqNo, byte[] input, int offset, int length) throws IOException {
        throw new TlsFatalAlert(AlertDescription.internal_error);
    }

    /**
     * Decrypts the given data.
     *
     * @param input  the input data
     * @param offset the input offset
     * @param length the input length
     * @return the decrypted data
     * @throws IOException if an error occurs
     */
    public byte[] decodeCiphertext(long seqNo, byte[] input, int offset, int length) throws IOException {
        // Check the input length.
        if (length < CHACHA20_POLY1305_TAG_SIZE) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Get the tag from the input.
        byte[] tag = new byte[CHACHA20_POLY1305_TAG_SIZE];
        System.arraycopy(input, offset + length - CHACHA20_POLY1305_TAG_SIZE, tag, 0, CHACHA20_POLY1305_TAG_SIZE);

        // Decrypt the input.
        byte[] plaintext = new byte[length - CHACHA20_POLY1305_TAG_SIZE];
        TlsUtils.chacha20Poly1305Decrypt(key, iv, seqNo, input, offset, length - CHACHA20_POLY1305_TAG_SIZE, plaintext, 0);

        // Verify the tag.
        if (!TlsUtils.constantTimeAreEqual(tag, TlsUtils.chacha20Poly1305(key, iv, seqNo, plaintext, 0, plaintext.length))) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }
}
```