```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public static byte[] decode(byte[] ciphertext, byte[] key, byte[] nonce) {
        // Create a ChaCha20 cipher object
        ChaCha20 cipher = new ChaCha20(key, nonce);

        // Decrypt the ciphertext
        byte[] plaintext = cipher.process(ciphertext);

        // Return the plaintext
        return plaintext;
    }
}
```