```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final TlsCipher cipher;
    private final TlsContext context;
    private final int macSize;

    public ChachaDecoder(TlsCipher cipher, TlsContext context) {
        this.cipher = cipher;
        this.context = context;
        this.macSize = cipher.getCipher().getMacSize();
    }

    public byte[] decode(byte[] input, int offset, int len) throws IOException {
        if (len < macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextLength = len - macSize;
        byte[] plaintext = new byte[plaintextLength];
        cipher.decodeCiphertext(offset, len, plaintext, 0);

        // Verify MAC
        byte[] receivedMac = new byte[macSize];
        System.arraycopy(input, offset + plaintextLength, receivedMac, 0, macSize);

        byte[] calculatedMac = cipher.calculateMac(macSize, input, offset, plaintextLength);

        if (!TlsUtils.constantTimeAreEqual(calculatedMac, receivedMac)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }

    public byte[] decodePlaintext(byte[] input, int offset, int len) throws IOException {
        if (len < macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextLength = len - macSize;
        byte[] plaintext = new byte[plaintextLength];
        System.arraycopy(input, offset, plaintext, 0, plaintextLength);

        // Verify MAC
        byte[] receivedMac = new byte[macSize];
        System.arraycopy(input, offset + plaintextLength, receivedMac, 0, macSize);

        byte[] calculatedMac = cipher.calculateMac(macSize, input, offset, plaintextLength);

        if (!TlsUtils.constantTimeAreEqual(calculatedMac, receivedMac)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }

    public int getPlaintextLimit(int ciphertextLimit) {
        return ciphertextLimit - macSize;
    }

    public int getCiphertextLimit(int plaintextLimit) {
        return plaintextLimit + macSize;
    }

    public int getMacSize() {
        return macSize;
    }
}
```