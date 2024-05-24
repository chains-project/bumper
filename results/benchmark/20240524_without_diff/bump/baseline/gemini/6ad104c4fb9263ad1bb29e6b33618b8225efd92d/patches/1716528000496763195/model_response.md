```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] data, int offset, int length) {
        // Check if the data is long enough for the ChaCha20 header.
        if (length < 12) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Extract the ChaCha20 header.
        byte[] header = new byte[12];
        System.arraycopy(data, offset, header, 0, 12);

        // Check if the ChaCha20 header is valid.
        if (!isValidChaCha20Header(header)) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Decode the data using ChaCha20.
        byte[] decodedData = new byte[length - 12];
        chacha20(header, data, offset + 12, decodedData, 0, length - 12);

        // Copy the decoded data to the output buffer.
        System.arraycopy(decodedData, 0, data, offset, length - 12);
    }

    private boolean isValidChaCha20Header(byte[] header) {
        // Check if the first byte is 0x43.
        if (header[0] != 0x43) {
            return false;
        }

        // Check if the second byte is 0x41.
        if (header[1] != 0x41) {
            return false;
        }

        // Check if the third byte is 0x50.
        if (header[2] != 0x50) {
            return false;
        }

        // Check if the fourth byte is 0x50.
        if (header[3] != 0x50) {
            return false;
        }

        // Check if the fifth byte is 0x00.
        if (header[4] != 0x00) {
            return false;
        }

        // Check if the sixth byte is 0x00.
        if (header[5] != 0x00) {
            return false;
        }

        // Check if the seventh byte is 0x00.
        if (header[6] != 0x00) {
            return false;
        }

        // Check if the eighth byte is 0x00.
        if (header[7] != 0x00) {
            return false;
        }

        // Check if the ninth byte is 0x00.
        if (header[8] != 0x00) {
            return false;
        }

        // Check if the tenth byte is 0x00.
        if (header[9] != 0x00) {
            return false;
        }

        // Check if the eleventh byte is 0x00.
        if (header[10] != 0x00) {
            return false;
        }

        // Check if the twelfth byte is 0x00.
        if (header[11] != 0x00) {
            return false;
        }

        return true;
    }

    private void chacha20(byte[] key, byte[] nonce, int inputOffset, byte[] output, int outputOffset, int length) {
        // Create a ChaCha20 cipher.
        ChaCha20 cipher = new ChaCha20();

        // Initialize the cipher with the key and nonce.
        cipher.init(key, nonce);

        // Process the input data.
        cipher.processBytes(inputOffset, output, outputOffset, length);
    }
}
```