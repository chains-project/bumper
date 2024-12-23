```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;
import java.util.Arrays;

public class ChachaDecoder {

    private final byte[] key;
    private final byte[] iv;
    private final int initialCounter;
    private final int nonceLength;

    public ChachaDecoder(byte[] key, byte[] iv, int initialCounter, int nonceLength) {
        this.key = key;
        this.iv = iv;
        this.initialCounter = initialCounter;
        this.nonceLength = nonceLength;
    }

    public byte[] decode(byte[] input) throws IOException {
        if (input.length < nonceLength) {
            throw new TlsFatalAlert(TlsProtocol.alert_decode_error);
        }

        byte[] nonce = Arrays.copyOfRange(input, 0, nonceLength);
        byte[] ciphertext = Arrays.copyOfRange(input, nonceLength, input.length);

        byte[] counter = new byte[8];
        ByteBuffer.wrap(counter).putInt(initialCounter);

        byte[] keyStream = ChaCha20.keystream(key, counter, nonce);

        byte[] plaintext = new byte[ciphertext.length];
        for (int i = 0; i < ciphertext.length; i++) {
            plaintext[i] = (byte) (ciphertext[i] ^ keyStream[i]);
        }

        return plaintext;
    }
}
```