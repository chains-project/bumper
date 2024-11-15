```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final TlsProtocol protocol;

    public ChachaDecoder(TlsProtocol protocol) {
        this.protocol = protocol;
    }

    public byte[] decode(byte[] in, int off, int len) throws IOException {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int key_block_size = protocol.getCipher().getKeyBlockSize();
        int iv_size = protocol.getCipher().getNonceSize();

        byte[] key_block = new byte[key_block_size];
        byte[] iv = new byte[iv_size];

        System.arraycopy(in, off, key_block, 0, key_block_size);
        System.arraycopy(in, off + key_block_size, iv, 0, iv_size);

        byte[] plaintext = new byte[len - key_block_size - iv_size];
        System.arraycopy(in, off + key_block_size + iv_size, plaintext, 0, plaintext.length);

        protocol.getCipher().init(CipherParameters.DECRYPTION_MODE, new ChaChaParameters(key_block, iv));

        protocol.getCipher().processBytes(plaintext, 0, plaintext.length, plaintext, 0);

        return plaintext;
    }
}
```