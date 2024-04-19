```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsStreamCipher;

import java.io.IOException;
import java.io.InputStream;

public class ChachaDecoder extends TlsStreamCipher {

    private static final int BLOCK_SIZE = 8;

    private final TlsCipher cipher;
    private final byte[] keyStream;
    private final int keyStreamPos;

    public ChachaDecoder(TlsCipher cipher, InputStream input, int keyStreamPos) throws IOException {
        super(cipher, input);
        this.cipher = cipher;
        this.keyStream = new byte[BLOCK_SIZE];
        this.keyStreamPos = keyStreamPos;
    }

    @Override
    public int doRead(byte[] buf, int offset, int len) throws IOException {
        if (len < 1) {
            return 0;
        }

        int bytesToRead = Math.min(len, keyStream.length - keyStreamPos);
        System.arraycopy(keyStream, keyStreamPos, buf, offset, bytesToRead);
        keyStreamPos += bytesToRead;

        if (keyStreamPos == keyStream.length) {
            cipher.generateKeyStream(keyStream, 0, keyStream.length);
            keyStreamPos = 0;
        }

        return bytesToRead;
    }

    @Override
    public byte[] encodePlaintext(long seqNo, byte type, byte[] plaintext, int offset, int len) throws IOException {
        throw new TlsFatalAlert(AlertDescription.internal_error);
    }

    @Override
    public int getPlaintextLimit(int ciphertextLimit) {
        return ciphertextLimit - TlsProtocol.RECORD_HEADER_LENGTH;
    }
}
```