```java
import org.bouncycastle.util.Arrays;

public class ChachaDecoder {

    public static byte[] decode(byte[] ciphertext, byte[] key, byte[] nonce, int macSize) {
        byte[] aad = new byte[0];
        byte[] plaintext = new byte[ciphertext.length - macSize];
        Chacha20Poly1305.chacha20Poly1305(key, nonce, aad, ciphertext, 0, ciphertext.length - macSize, plaintext, 0);
        return plaintext;
    }
}
```