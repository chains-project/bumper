```java
import org.bouncycastle.util.Arrays;

public class ChachaDecoder {

    public ChachaDecoder(byte[] key, byte[] nonce) {
        this.key = key;
        this.nonce = nonce;
    }

    public byte[] decode(byte[] ciphertext) {
        byte[] plaintext = new byte[ciphertext.length];
        Arrays.copy(ciphertext, 0, plaintext, 0, ciphertext.length);
        return plaintext;
    }

    private final byte[] key;
    private final byte[] nonce;
}
```