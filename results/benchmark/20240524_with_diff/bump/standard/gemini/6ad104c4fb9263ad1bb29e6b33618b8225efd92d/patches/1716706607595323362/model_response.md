```java
import org.bouncycastle.util.Arrays;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public ChachaDecoder(byte[] key, int initialCounter) {
        this.key = key;
        this.initialCounter = initialCounter;
    }

    public byte[] decode(byte[] ciphertext, int offset, int len) {
        byte[] plaintext = new byte[len];
        chacha.processBytes(ciphertext, offset, len, plaintext, 0);
        return plaintext;
    }

    private final byte[] key;
    private final int initialCounter;
    private final ChaCha chacha = new ChaCha();
}
```