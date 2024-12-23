```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final TlsCipher cipher;
    private final TlsContext context;
    private final int macSize;
    private final int plaintextLimit;

    public ChachaDecoder(TlsCipher cipher, TlsContext context, int macSize, int plaintextLimit) {
        this.cipher = cipher;
        this.context = context;
        this.macSize = macSize;
        this.plaintextLimit = plaintextLimit;
    }

    public byte[] decode(byte[] buf, int off, int len) throws IOException {
        if (len < macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextSize = len - macSize;
        if (plaintextSize > plaintextLimit) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] mac = new byte[macSize];
        System.arraycopy(buf, off + plaintextSize, mac, 0, macSize);

        byte[] plaintext = new byte[plaintextSize];
        System.arraycopy(buf, off, plaintext, 0, plaintextSize);

        cipher.init(context, false, plaintext);

        int actualMacSize = cipher.getMacSize();
        if (actualMacSize != macSize) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }

        byte[] calculatedMac = new byte[macSize];
        cipher.doFinal(calculatedMac, 0);

        if (!TlsUtils.constantTimeAreEqual(calculatedMac, mac)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }
}
```