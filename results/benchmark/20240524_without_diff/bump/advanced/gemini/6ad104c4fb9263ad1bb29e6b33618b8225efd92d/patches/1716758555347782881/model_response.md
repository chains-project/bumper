```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder implements TlsCipher {

    private static final int CHACHA_BLOCK_SIZE = 64;

    private final TlsContext context;
    private final TlsCipher underlyingCipher;
    private final int cipherKeySize;
    private final int macSize;
    private final boolean isRead;

    private byte[] keyStreamBuffer;
    private int keyStreamPos;

    public ChachaDecoder(TlsContext context, TlsCipher underlyingCipher, int cipherKeySize, int macSize,
            boolean isRead) {
        this.context = context;
        this.underlyingCipher = underlyingCipher;
        this.cipherKeySize = cipherKeySize;
        this.macSize = macSize;
        this.isRead = isRead;
    }

    @Override
    public int getCiphertextDecodeLimit(int plaintextLength) {
        return plaintextLength + macSize;
    }

    @Override
    public int getPlaintextLimit(int ciphertextLength) {
        return ciphertextLength - macSize;
    }

    @Override
    public void init(TlsContext context, int encryptionLevel) {
        this.underlyingCipher.init(context, encryptionLevel);
    }

    @Override
    public byte[] decodeCiphertext(int seqNo, short type, ByteBuffer ciphertext, int offset, int len)
            throws IOException {
        int plaintextLength = getPlaintextLimit(len);
        byte[] plaintext = new byte[plaintextLength];

        if (keyStreamPos + len > keyStreamBuffer.length) {
            keyStreamBuffer = new byte[keyStreamPos + len];
        }

        underlyingCipher.decodeCiphertext(seqNo, type, ciphertext, offset, len, keyStreamBuffer, keyStreamPos);
        keyStreamPos += len;

        int end = plaintextLength - macSize;
        for (int i = 0; i < end; i++) {
            plaintext[i] = (byte) (ciphertext.get(offset + i) ^ keyStreamBuffer[i]);
        }

        if (isRead) {
            checkMac(ciphertext, offset + end, macSize, plaintext, 0, end);
        }

        return plaintext;
    }

    private void checkMac(ByteBuffer ciphertext, int offset, int macLength, byte[] plaintext, int plaintextOffset,
            int plaintextLength) throws IOException {
        byte[] receivedMac = new byte[macLength];
        ciphertext.position(offset);
        ciphertext.get(receivedMac);

        byte[] calculatedMac = calculateMac(plaintext, plaintextOffset, plaintextLength);

        if (!TlsUtils.constantTimeAreEqual(calculatedMac, receivedMac)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }
    }

    private byte[] calculateMac(byte[] plaintext, int plaintextOffset, int plaintextLength) {
        byte[] mac = new byte[macSize];

        int macSeqNo = context.getReceiveSequenceNumber() & 0xFFFFFFFFL;
        TlsProtocol.writeUint64(macSeqNo, mac, 0);
        TlsProtocol.writeUint16(plaintextLength, mac, 8);

        underlyingCipher.calculateMac(mac, 0, mac.length, plaintext, plaintextOffset, plaintextLength);

        return mac;
    }
}
```