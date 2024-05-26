```java
import org.bouncycastle.util.Arrays;

public class ChachaDecoder {

    public static byte[] decode(byte[] ciphertext, byte[] key, byte[] nonce, int macSize) {
        byte[] plaintext = new byte[ciphertext.length - macSize];
        Chacha.cha20Poly1305(ciphertext, plaintext, key, nonce, 0);
        return plaintext;
    }

}
```