```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsCompression;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsStreamCipher;

public class ChachaDecoder {

    private final TlsContext context;
    private final TlsStreamCipher decryptCipher;

    public ChachaDecoder(TlsContext context, TlsStreamCipher decryptCipher) {
        this.context = context;
        this.decryptCipher = decryptCipher;
    }

    public byte[] decode(byte[] buf, int off, int len) {
        if (len < 4) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plainTextLength = TlsUtils.readUint24(buf, off);
        off += 3;
        len -= 3;

        if (plainTextLength > len) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] plainText = new byte[plainTextLength];
        decryptCipher.init(context, false);
        decryptCipher.processBytes(buf, off, plainTextLength, plainText, 0);

        if (TlsProtocol.versionSupportsTruncatedHMac(context.getServerVersion())) {
            TlsCipher cipher = context.getSecurityParameters().getCipher();
            int macSize = cipher.getMacSize();
            if (macSize > 0) {
                int check = TlsUtils.readUint16(plainText, plainTextLength - macSize);
                int received = TlsUtils.calculateCheck(plainText, 0, plainTextLength - macSize, context.getSecurityParameters().getServerRandom(),
                        context.getSecurityParameters().getClientRandom(), macSize);
                if (check != received) {
                    throw new TlsFatalAlert(AlertDescription.bad_record_mac);
                }
            }
        } else {
            TlsUtils.checkUint16(plainText, plainTextLength);
        }

        return plainText;
    }

    public void init(TlsContext context, TlsCompression tlsCompression) {
        this.context = context;
        this.decryptCipher = context.getStreamCipher();
    }

}
```