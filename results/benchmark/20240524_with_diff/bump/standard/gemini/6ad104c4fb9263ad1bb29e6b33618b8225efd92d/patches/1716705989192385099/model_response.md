```java
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;

public class ChachaDecoder {

    private final byte[] key;
    private final byte[] iv;

    public ChachaDecoder(byte[] key, byte[] iv) {
        this.key = key;
        this.iv = iv;
    }

    public byte[] decode(byte[] data) throws IOException {
        if (data.length < 16) {
            throw new IllegalArgumentException("Data must be at least 16 bytes long");
        }

        byte[] nonce = new byte[12];
        System.arraycopy(iv, 0, nonce, 0, 4);
        System.arraycopy(data, 0, nonce, 4, 8);

        byte[] counter = new byte[8];
        System.arraycopy(data, 8, counter, 0, 8);

        byte[] ciphertext = new byte[data.length - 16];
        System.arraycopy(data, 16, ciphertext, 0, ciphertext.length);

        return Chacha.decrypt(key, nonce, counter, ciphertext);
    }
}
```