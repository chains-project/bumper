```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsUtils;

import java.io.IOException;
import java.util.Arrays;

public class ChachaDecoder {

    private final TlsContext context;
    private final TlsCipher decryptCipher;
    private final int ivSize;

    public ChachaDecoder(TlsContext context, TlsCipher decryptCipher) {
        this.context = context;
        this.decryptCipher = decryptCipher;
        this.ivSize = decryptCipher.getCipher().getAlgorithm().getIVSize();
    }

    public byte[] decode(byte[] buf, int off, int len) throws IOException {
        if (len < ivSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] iv = Arrays.copyOfRange(buf, off, off + ivSize);
        off += ivSize;
        len -= ivSize;

        byte[] output = new byte[len];
        decryptCipher.init(context, iv, off, len, output, 0);
        decryptCipher.doFinal(output, 0);

        return output;
    }

    public byte[] decode(byte[] buf) throws IOException {
        return decode(buf, 0, buf.length);
    }
}
```