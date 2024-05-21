```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsCompression;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsCredentials;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsSession;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.util.Vector;

public class ChachaDecoder extends AbstractTlsCipher {

    protected TlsCipher underlyingCipher;

    public ChachaDecoder(InputStream input, OutputStream output,
                          TlsSession session) throws IOException {
        super(input, output, session);

        this.underlyingCipher = session.getCipher();
    }

    @Override
    public int getCiphertextDecodeLimit(int plaintextLimit) {
        return underlyingCipher.getCiphertextDecodeLimit(plaintextLimit);
    }

    @Override
    public int getCiphertextEncodeLimit(int plaintextLength) {
        return underlyingCipher.getCiphertextEncodeLimit(plaintextLength);
    }

    @Override
    public void init(TlsContext context, int readAhead) throws IOException {
        underlyingCipher.init(context, readAhead);
    }

    @Override
    public byte[] decodeCiphertext(int seqNo, byte[] ciphertext, int offset, int len)
            throws IOException {
        return underlyingCipher.decodeCiphertext(seqNo, ciphertext, offset, len);
    }

    @Override
    public byte[] encodePlaintext(int type, byte[] plaintext, int offset, int len)
            throws IOException {
        return underlyingCipher.encodePlaintext(type, plaintext, offset, len);
    }

}
```