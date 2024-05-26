```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsSession;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final TlsSession session;

    public ChachaDecoder(TlsSession session) {
        this.session = session;
    }

    public byte[] decode(byte[] data, int offset, int len) throws IOException {
        if (len < 8) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }

        int keyBlockLength = data[offset] & 0xff;
        int nonceLength = data[offset + 1] & 0xff;

        if (keyBlockLength < 1 || keyBlockLength > 255) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }

        if (nonceLength < 1 || nonceLength > 255) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }

        int macLength = data[offset + 2] & 0xff;
        if (macLength < 1 || macLength > 255) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }

        int plaintextLength = len - 8 - keyBlockLength - nonceLength - macLength;
        if (plaintextLength < 0) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }

        int keyBlockOffset = offset + 3;
        int nonceOffset = keyBlockOffset + keyBlockLength;
        int macOffset = nonceOffset + nonceLength;
        int plaintextOffset = macOffset + macLength;

        byte[] keyBlock = new byte[keyBlockLength];
        System.arraycopy(data, keyBlockOffset, keyBlock, 0, keyBlockLength);

        byte[] nonce = new byte[nonceLength];
        System.arraycopy(data, nonceOffset, nonce, 0, nonceLength);

        byte[] mac = new byte[macLength];
        System.arraycopy(data, macOffset, mac, 0, macLength);

        byte[] plaintext = new byte[plaintextLength];
        System.arraycopy(data, plaintextOffset, plaintext, 0, plaintextLength);

        // Check the MAC
        byte[] calculatedMac = session.getCrypto().createNonceRandom().generateNonce(macLength);
        if (!TlsUtils.constantTimeAreEqual(calculatedMac, mac)) {
            throw new TlsFatalAlert(TlsFatalAlert.BAD_RECORD_MAC);
        }

        // Decrypt the plaintext
        byte[] decryptedPlaintext = session.getCrypto().chacha20Decrypt(keyBlock, nonce, plaintext);

        // Check the padding
        int paddingLength = decryptedPlaintext[decryptedPlaintext.length - 1];
        if (paddingLength < 1 || paddingLength > 255) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }

        for (int i = decryptedPlaintext.length - paddingLength - 1; i < decryptedPlaintext.length - 1; i++) {
            if (decryptedPlaintext[i] != paddingLength) {
                throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
            }
        }

        return TlsUtils.copyOfRange(decryptedPlaintext, 0, decryptedPlaintext.length - paddingLength - 1);
    }
}
```