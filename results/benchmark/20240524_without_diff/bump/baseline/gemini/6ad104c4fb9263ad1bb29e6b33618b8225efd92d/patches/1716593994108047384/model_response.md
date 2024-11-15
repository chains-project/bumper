```java
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsProtocol;

import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class ChachaDecoder {

    private final TlsContext context;
    private final InputStream input;
    private final OutputStream output;
    private final int macSize;
    private final int fixedIvLength;
    private Cipher cipher;
    private SecretKeySpec key;
    private IvParameterSpec iv;

    public ChachaDecoder(TlsContext context, InputStream input, OutputStream output, int macSize) throws IOException {
        this.context = context;
        this.input = input;
        this.output = output;
        this.macSize = macSize;
        this.fixedIvLength = context.getServerVersion().isSSL()
                ? 0
                : TlsProtocol.RECORD_HEADER_LENGTH;
    }

    public void init(TlsCipher cipher, SecretKeySpec key, IvParameterSpec iv) throws IOException {
        this.cipher = cipher;
        this.key = key;
        this.iv = iv;
    }

    public int decode(byte[] buf, int off, int len) throws IOException {
        if (len < macSize) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int plaintextLength = len - macSize;
        byte[] mac = new byte[macSize];
        System.arraycopy(buf, off + plaintextLength, mac, 0, macSize);

        byte[] plaintext = new byte[plaintextLength];
        System.arraycopy(buf, off, plaintext, 0, plaintextLength);

        cipher.init(Cipher.DECRYPT_MODE, key, iv);
        cipher.doFinal(plaintext, 0, plaintextLength, plaintext, 0);

        return plaintextLength;
    }

    public void close() throws IOException {
        if (cipher != null) {
            cipher = null;
            key = null;
            iv = null;
        }
    }
}
```