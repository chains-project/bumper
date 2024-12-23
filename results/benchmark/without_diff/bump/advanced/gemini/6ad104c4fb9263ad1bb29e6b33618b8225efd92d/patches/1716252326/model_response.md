```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsUtils;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {
    private final ByteBuffer buffer = ByteBuffer.allocate(256);
    private final int keyLength;
    private final int nonceLength;
    private final int macLength;
    private final int recordSizeLimit;
    private final int aeadAlgorithm;
    private final byte[] key;
    private final byte[] nonce;
    private final byte[] mac;

    public ChachaDecoder(int keyLength, int nonceLength, int macLength, int recordSizeLimit, int aeadAlgorithm, byte[] key, byte[] nonce, byte[] mac) {
        this.keyLength = keyLength;
        this.nonceLength = nonceLength;
        this.macLength = macLength;
        this.recordSizeLimit = recordSizeLimit;
        this.aeadAlgorithm = aeadAlgorithm;
        this.key = key;
        this.nonce = nonce;
        this.mac = mac;
    }

    public byte[] decode(byte[] record) throws IOException {
        if (record.length < 256) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        buffer.clear();
        buffer.put(record);
        buffer.flip();

        int plaintextLength = buffer.getInt(0);
        if (plaintextLength > recordSizeLimit) {
            throw new TlsFatalAlert(AlertDescription.record_overflow);
        }

        int macOffset = buffer.position() + plaintextLength;
        int ciphertextLength = macOffset - buffer.position() - macLength;

        byte[] ciphertext = new byte[ciphertextLength];
        buffer.position(buffer.position() + 4);
        buffer.get(ciphertext, 0, ciphertextLength);

        byte[] computedMac = TlsUtils.calculateMac(aeadAlgorithm, key, nonce, ciphertext, 0, ciphertextLength);

        if (!TlsUtils.constantTimeAreEqual(mac, 0, computedMac, 0, macLength)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        byte[] plaintext = new byte[plaintextLength];
        TlsUtils.decrypt(aeadAlgorithm, key, nonce, ciphertext, 0, ciphertextLength, plaintext, 0);

        return plaintext;
    }
}
```