```java
import org.bouncycastle.crypto.tls.AlertLevel;
import org.bouncycastle.crypto.tls.AlertMessage;

public class ChachaDecoder {

    public void decode(byte[] data, int offset, int len) {
        if (len < 5) {
            throw new IllegalArgumentException("Insufficient data for ChaCha20Poly1305");
        }

        int cipherTextLength = len - 16;
        byte[] cipherText = new byte[cipherTextLength];
        System.arraycopy(data, offset + 5, cipherText, 0, cipherTextLength);

        byte[] tag = new byte[16];
        System.arraycopy(data, offset + 5 + cipherTextLength, tag, 0, 16);

        // Check for the presence of the ChaCha20Poly1305 algorithm identifier
        if (data[offset] != 0x07 || data[offset + 1] != 0x00 || data[offset + 2] != 0x00 || data[offset + 3] != 0x00) {
            throw new IllegalArgumentException("Invalid ChaCha20Poly1305 algorithm identifier");
        }

        // Check for the presence of the ChaCha20Poly1305 nonce
        if (data[offset + 4] != 0x00 || data[offset + 5] != 0x00 || data[offset + 6] != 0x00 || data[offset + 7] != 0x00) {
            throw new IllegalArgumentException("Invalid ChaCha20Poly1305 nonce");
        }

        // Create an AlertMessage with an appropriate description
        AlertMessage alertMessage = new AlertMessage(AlertLevel.fatal, AlertDescription.decrypt_error);

        // Throw an exception with the AlertMessage as the cause
        throw new IllegalArgumentException("ChaCha20Poly1305 decryption failed", alertMessage);
    }
}
```