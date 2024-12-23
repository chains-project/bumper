```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder {

    private final byte[] key;
    private final byte[] iv;

    public ChachaDecoder(byte[] key, byte[] iv) {
        this.key = key;
        this.iv = iv;
    }

    public byte[] decode(byte[] data) throws IOException {
        // Create a new ChaCha20 cipher using the provided key and IV.
        final ChaCha20 cipher = new ChaCha20(key, iv);

        // Create a new byte array to hold the decrypted data.
        final byte[] decryptedData = new byte[data.length];

        // Decrypt the data using the ChaCha20 cipher.
        cipher.processBytes(data, 0, data.length, decryptedData, 0);

        // Return the decrypted data.
        return decryptedData;
    }
}
```