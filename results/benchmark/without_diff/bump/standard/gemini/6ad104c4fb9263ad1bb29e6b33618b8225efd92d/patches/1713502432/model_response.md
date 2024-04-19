```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;

import java.io.IOException;

public class ChachaDecoder {

    private final TlsCipher cipher;

    public ChachaDecoder(TlsCipher cipher) {
        this.cipher = cipher;
    }

    public byte[] decode(byte[] input, int inputOffset, int inputLength) throws IOException {
        // Check if the input length is valid.
        if (inputLength < 16) {
            throw new IllegalArgumentException("Input length must be at least 16 bytes.");
        }

        // Create a new byte array to hold the decoded data.
        byte[] output = new byte[inputLength - 16];

        // Decrypt the input data.
        cipher.decrypt(input, inputOffset + 16, inputLength - 16, output, 0);

        // Return the decoded data.
        return output;
    }
}
```