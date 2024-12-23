```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;

public class ChachaDecoder {

    private final byte[] key;
    private final byte[] iv;

    public ChachaDecoder(byte[] key, byte[] iv) {
        this.key = key;
        this.iv = iv;
    }

    public byte[] decode(byte[] input) throws IOException {
        if (input.length < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] nonce = new byte[12];
        System.arraycopy(input, 0, nonce, 0, 12);

        byte[] ciphertext = new byte[input.length - 16];
        System.arraycopy(input, 16, ciphertext, 0, ciphertext.length);

        byte[] plaintext = new byte[ciphertext.length];
        ChaCha20.decrypt(key, nonce, ciphertext, 0, plaintext, 0, plaintext.length);

        return plaintext;
    }
}
```