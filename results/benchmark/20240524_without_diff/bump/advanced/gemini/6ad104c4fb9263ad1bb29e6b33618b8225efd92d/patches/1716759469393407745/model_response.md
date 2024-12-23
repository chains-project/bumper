```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsCompression;
import org.bouncycastle.crypto.tls.TlsSession;
import org.bouncycastle.crypto.tls.TlsInputStream;
import org.bouncycastle.crypto.tls.TlsOutputStream;
import org.bouncycastle.crypto.tls.TlsUtils;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsCompression;
import org.bouncycastle.crypto.tls.TlsSession;
import org.bouncycastle.crypto.tls.TlsInputStream;
import org.bouncycastle.crypto.tls.TlsOutputStream;
import org.bouncycastle.crypto.tls.TlsUtils;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class ChachaDecoder {

    private TlsSession session;
    private TlsInputStream input;

    public ChachaDecoder(TlsSession session, InputStream input) {
        this.session = session;
        this.input = new TlsInputStream(input);
    }

    public byte[] decode(byte[] data) throws IOException {
        // Check if the data is encrypted with ChaCha20
        if (session.getCipher().getAlgorithm() == TlsCipher.chacha20_poly1305) {
            // Decrypt the data using the session's ChaCha20 cipher
            return session.getCipher().decodeCiphertext(data, 0, data.length);
        } else {
            // If the data is not encrypted with ChaCha20, throw an exception
            throw new TlsFatalAlert(TlsFatalAlert.decrypt_error);
        }
    }

    public void close() throws IOException {
        input.close();
    }
}
```