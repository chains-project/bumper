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
        this.macSize = cipher.getMacSize();
    }

    public byte[] decode(byte[] buf, int off, int len) throws IOException {
        if (len < macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plainTextLength = len - macSize;
        byte[] plainText = new byte[plainTextLength];
        cipher.decodeCiphertext(buf, off, len, plainText, 0);

        int receivedMac = context.getSecurityParameters().getPeerVerifyDataLength();
        if (receivedMac != macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int calculatedMac = TlsProtocol.calculateVerifyData(context, plainText, 0, plainTextLength);
        if (calculatedMac != context.getSecurityParameters().getPeerVerifyData()[0]) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plainText;
    }

    public byte[] decodeCiphertext(byte[] buf, int off, int len) throws IOException {
        if (len < macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plainTextLength = len - macSize;
        byte[] plainText = new byte[plainTextLength];
        cipher.decodeCiphertext(buf, off, len, plainText, 0);

        int receivedMac = context.getSecurityParameters().getPeerVerifyDataLength();
        if (receivedMac != macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int calculatedMac = TlsProtocol.calculateVerifyData(context, plainText, 0, plainTextLength);
        if (calculatedMac != context.getSecurityParameters().getPeerVerifyData()[0]) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        return plainText;
    }
}
```