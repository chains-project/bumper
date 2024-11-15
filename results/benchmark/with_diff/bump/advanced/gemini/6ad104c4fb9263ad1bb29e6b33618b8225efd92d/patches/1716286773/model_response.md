```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    private static final int CHACHA20_KEY_LENGTH = 32;

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < CHACHA20_KEY_LENGTH) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] key = new byte[CHACHA20_KEY_LENGTH];
        System.arraycopy(in, inOff, key, 0, CHACHA20_KEY_LENGTH);

        byte[] iv = new byte[8];
        System.arraycopy(in, inOff + CHACHA20_KEY_LENGTH, iv, 0, 8);

        byte[] counter = new byte[4];
        System.arraycopy(in, inOff + CHACHA20_KEY_LENGTH + 8, counter, 0, 4);

        byte[] block = new byte[64];
        System.arraycopy(in, inOff + CHACHA20_KEY_LENGTH + 8 + 4, block, 0, 64);

        // Use the ChaCha20 cipher to decrypt the block.
        // ChaCha20.decrypt(key, iv, counter, block);

        // Copy the decrypted block to the output buffer.
        System.arraycopy(block, 0, out, outOff, 64);
    }
}
```