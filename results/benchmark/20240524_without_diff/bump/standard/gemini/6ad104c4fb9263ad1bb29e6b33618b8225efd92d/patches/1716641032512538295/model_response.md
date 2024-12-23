```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final int keyLength;
    private final int nonceLength;
    private final byte[] key;
    private final byte[] nonce;
    private final TlsProtocol protocol;

    public ChachaDecoder(int keyLength, int nonceLength, byte[] key, byte[] nonce, TlsProtocol protocol) {
        this.keyLength = keyLength;
        this.nonceLength = nonceLength;
        this.key = key;
        this.nonce = nonce;
        this.protocol = protocol;
    }

    public byte[] decode(byte[] in, int inOff, int len) throws IOException {
        if (len < 1) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextLength = len - 1;
        byte[] plaintext = new byte[plaintextLength];

        // Extract the additional data
        byte additionalData = in[inOff];
        inOff++;
        len--;

        // Check the additional data
        if (additionalData != 0) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Check the length of the input
        if (len < keyLength + nonceLength + plaintextLength) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Extract the key and nonce
        byte[] key = new byte[keyLength];
        byte[] nonce = new byte[nonceLength];
        System.arraycopy(in, inOff, key, 0, keyLength);
        inOff += keyLength;
        System.arraycopy(in, inOff, nonce, 0, nonceLength);
        inOff += nonceLength;

        // Decrypt the plaintext
        protocol.chacha20Poly1305(key, nonce, in, inOff, plaintextLength, plaintext, 0);

        return plaintext;
    }
}
```