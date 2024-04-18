```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final int cipherKeyLen;
    private final int macKeyLen;
    private final int recordSeq;
    private final byte[] clientWriteKey;
    private final byte[] serverWriteKey;
    private final byte[] clientWriteIV;
    private final byte[] serverWriteIV;

    public ChachaDecoder(int cipherKeyLen, int macKeyLen, int recordSeq, byte[] clientWriteKey, byte[] serverWriteKey, byte[] clientWriteIV, byte[] serverWriteIV) {
        this.cipherKeyLen = cipherKeyLen;
        this.macKeyLen = macKeyLen;
        this.recordSeq = recordSeq;
        this.clientWriteKey = clientWriteKey;
        this.serverWriteKey = serverWriteKey;
        this.clientWriteIV = clientWriteIV;
        this.serverWriteIV = serverWriteIV;
    }

    public byte[] decode(byte[] input) throws IOException {
        if (input.length < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        ByteBuffer buffer = ByteBuffer.wrap(input);
        int length = buffer.getInt();
        if (length + 16 > input.length) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] content = new byte[length];
        buffer.get(content);

        byte[] mac = new byte[16];
        buffer.get(mac);

        byte[] key = recordSeq % 2 == 0 ? clientWriteKey : serverWriteKey;
        byte[] iv = recordSeq % 2 == 0 ? clientWriteIV : serverWriteIV;
        byte[] nonce = new byte[12];
        System.arraycopy(iv, 0, nonce, 0, 4);
        System.arraycopy(new byte[]{0, 0, 0, (byte) recordSeq}, 0, nonce, 4, 4);
        System.arraycopy(iv, 4, nonce, 8, 4);

        byte[] plaintext = ChachaUtils.chacha20(key, nonce, content);

        if (!verifyMac(plaintext, mac)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }

    private boolean verifyMac(byte[] plaintext, byte[] mac) {
        byte[] expectedMac = ChachaUtils.poly1305(macKeyLen, mac, plaintext);
        return TlsUtils.constantTimeAreEqual(mac, expectedMac);
    }
}
```