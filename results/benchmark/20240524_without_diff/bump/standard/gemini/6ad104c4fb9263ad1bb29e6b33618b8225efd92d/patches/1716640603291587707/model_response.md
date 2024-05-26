```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public ChachaDecoder(byte[] key, byte[] nonce) {
        this.key = key;
        this.nonce = nonce;
    }

    public byte[] decode(byte[] input) {
        // Create a new ChaCha20 cipher with the given key and nonce.
        ChaCha20 cipher = new ChaCha20(key, nonce);

        // Initialize the cipher with the first 8 bytes of the input.
        cipher.init(input, 0, 8);

        // Decrypt the remaining bytes of the input.
        byte[] output = new byte[input.length - 8];
        cipher.processBytes(input, 8, output, 0, output.length);

        return output;
    }

    private final byte[] key;
    private final byte[] nonce;
}
```