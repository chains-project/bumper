```java
import org.bouncycastle.util.Arrays;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public ChachaDecoder(byte[] key, byte[] nonce) {
        this.key = key;
        this.nonce = nonce;
    }

    public byte[] decode(byte[] ciphertext) {
        byte[] plaintext = new byte[ciphertext.length];
        chacha.process(nonce, key, plaintext, 0, ciphertext.length);
        return plaintext;
    }

    private final byte[] key;
    private final byte[] nonce;
    private final Chacha chacha = new Chacha();
}
```