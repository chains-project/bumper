```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsUtils;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final TlsContext context;
    private final int macSize;
    private final byte[] recordMAC;
    private final byte[] aad;
    private final byte[] nonce;

    public ChachaDecoder(TlsContext context, int macSize, byte[] recordMAC, byte[] aad, byte[] nonce) {
        this.context = context;
        this.macSize = macSize;
        this.recordMAC = recordMAC;
        this.aad = aad;
        this.nonce = nonce;
    }

    public byte[] decode(byte[] buf, int off, int len) throws IOException {
        if (len < macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextLength = len - macSize;
        byte[] plaintext = new byte[plaintextLength];

        TlsUtils.chacha20Poly1305(context.getSecurityParameters().getCurrentPRFHash(), recordMAC, aad, nonce,
                buf, off, plaintextLength, plaintext, 0);

        if (!TlsUtils.constantTimeAreEqual(macSize, plaintext, plaintextLength, buf, off + plaintextLength)) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plaintext;
    }
}
```