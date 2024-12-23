```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.io.OutputStream;

public class ChachaDecoder {

    private final TlsContext context;
    private final TlsCipher decryptCipher;

    public ChachaDecoder(TlsContext context, TlsCipher decryptCipher) {
        this.context = context;
        this.decryptCipher = decryptCipher;
    }

    public void decode(OutputStream output, byte[] buf, int off, int len) throws IOException {
        if (len < 8) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int macSize = decryptCipher.getMacSize();
        int plaintextLength = len - macSize;

        // Check the MAC
        int receivedMac = TlsUtils.readUint32(buf, off + plaintextLength);
        int calculatedMac = decryptCipher.calculateMac(buf, off, plaintextLength);

        if (receivedMac != calculatedMac) {
            throw new TlsFatalAlert(AlertDescription.bad_record_mac);
        }

        // Decrypt the data
        decryptCipher.decryptData(buf, off, plaintextLength, buf, off);

        // Remove the MAC
        output.write(buf, off, plaintextLength);
    }
}
```