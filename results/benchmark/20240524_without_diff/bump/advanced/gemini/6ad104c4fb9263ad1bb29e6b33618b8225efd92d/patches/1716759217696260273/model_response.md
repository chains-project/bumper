```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsUtils;

import java.io.IOException;
import java.nio.ByteBuffer;

/**
 * An implementation of {@link org.bouncycastle.crypto.tls.TlsCipher} based on the ChaCha20 stream cipher.
 *
 * @see <a href="https://tools.ietf.org/html/rfc7905">RFC 7905</a>
 */
public class ChachaDecoder implements TlsCipher {

    private static final int CHACHA_KEY_LENGTH = 32;
    private static final int CHACHA_NONCE_LENGTH = 12;
    private static final int CHACHA_POLY1305_MAC_LENGTH = 16;

    private final ChachaEngine chachaEngine;
    private final Poly1305Engine poly1305Engine;
    private final boolean isRead;

    private ByteBuffer pendingInput = ByteBuffer.allocate(0);
    private ByteBuffer pendingOutput = ByteBuffer.allocate(0);

    public ChachaDecoder(ChachaEngine chachaEngine, Poly1305Engine poly1305Engine, boolean isRead) {
        this.chachaEngine = chachaEngine;
        this.poly1305Engine = poly1305Engine;
        this.isRead = isRead;
    }

    @Override
    public int getCiphertextDecodeLimit(int plaintextLength) {
        return plaintextLength + CHACHA_POLY1305_MAC_LENGTH;
    }

    @Override
    public int getCiphertextEncodeLimit(int plaintextLength) {
        return plaintextLength + CHACHA_POLY1305_MAC_LENGTH;
    }

    @Override
    public int getPlaintextLimit(int ciphertextLength) {
        return ciphertextLength - CHACHA_POLY1305_MAC_LENGTH;
    }

    @Override
    public void init(TlsContext context, int encryptionLevel) {
        this.chachaEngine.init(context, encryptionLevel, isRead);
        this.poly1305Engine.init(context, encryptionLevel, isRead);
    }

    @Override
    public byte[] decodeCiphertext(int type, byte[] ciphertext, int offset, int len) throws IOException {
        if (len < CHACHA_POLY1305_MAC_LENGTH) {
            throw new TlsFatalAlert(TlsFatalAlert.bad_record_mac);
        }

        int plaintextLength = len - CHACHA_POLY1305_MAC_LENGTH;
        byte[] plaintext = new byte[plaintextLength];

        // Process the pending input
        int pendingInputLength = pendingInput.remaining();
        if (pendingInputLength > 0) {
            int bytesToProcess = Math.min(pendingInputLength, len);
            pendingInput.put(ciphertext, offset, bytesToProcess);
            offset += bytesToProcess;
            len -= bytesToProcess;
        }

        // Process the current input
        if (len > 0) {
            // Decrypt the ciphertext
            chachaEngine.processBytes(ciphertext, offset, len, plaintext, 0);

            // Verify the MAC
            byte[] mac = new byte[CHACHA_POLY1305_MAC_LENGTH];
            System.arraycopy(ciphertext, offset + len, mac, 0, CHACHA_POLY1305_MAC_LENGTH);
            if (!poly1305Engine.verify(plaintext, 0, plaintextLength, mac)) {
                throw new TlsFatalAlert(TlsFatalAlert.bad_record_mac);
            }
        }

        // Process the pending output
        int pendingOutputLength = pendingOutput.remaining();
        if (pendingOutputLength > 0) {
            int bytesToProcess = Math.min(pendingOutputLength, plaintextLength);
            pendingOutput.put(plaintext, 0, bytesToProcess);
            System.arraycopy(plaintext, bytesToProcess, plaintext, 0, plaintextLength - bytesToProcess);
            plaintextLength -= bytesToProcess;
        }

        // Update the pending input and output
        pendingInput = ByteBuffer.allocate(0);
        pendingOutput = ByteBuffer.wrap(plaintext, plaintextLength, plaintextLength);

        return plaintext;
    }

    @Override
    public byte[] encodePlaintext(int type, byte[] plaintext, int offset, int len) throws IOException {
        if (len < CHACHA_POLY1305_MAC_LENGTH) {
            throw new TlsFatalAlert(TlsFatalAlert.bad_record_mac);
        }

        int ciphertextLength = len + CHACHA_POLY1305_MAC_LENGTH;
        byte[] ciphertext = new byte[ciphertextLength];

        // Process the pending input
        int pendingInputLength = pendingInput.remaining();
        if (pendingInputLength > 0) {
            int bytesToProcess = Math.min(pendingInputLength, len);
            pendingInput.put(plaintext, offset, bytesToProcess);
            offset += bytesToProcess;
            len -= bytesToProcess;
        }

        // Process the current input
        if (len > 0) {
            // Encrypt the plaintext
            chachaEngine.processBytes(plaintext, offset, len, ciphertext, 0);

            // Generate the MAC
            byte[] mac = new byte[CHACHA_POLY1305_MAC_LENGTH];
            poly1305Engine.update(ciphertext, 0, len);
            poly1305Engine.doFinal(mac, 0);
            System.arraycopy(mac, 0, ciphertext, len, CHACHA_POLY1305_MAC_LENGTH);
        }

        // Process the pending output
        int pendingOutputLength = pendingOutput.remaining();
        if (pendingOutputLength > 0) {
            int bytesToProcess = Math.min(pendingOutputLength, ciphertextLength);
            pendingOutput.put(ciphertext, 0, bytesToProcess);
            System.arraycopy(ciphertext, bytesToProcess, ciphertext, 0, ciphertextLength - bytesToProcess);
            ciphertextLength -= bytesToProcess;
        }

        // Update the pending input and output
        pendingInput = ByteBuffer.allocate(0);
        pendingOutput = ByteBuffer.wrap(ciphertext, ciphertextLength, ciphertextLength);

        return ciphertext;
    }
}
```