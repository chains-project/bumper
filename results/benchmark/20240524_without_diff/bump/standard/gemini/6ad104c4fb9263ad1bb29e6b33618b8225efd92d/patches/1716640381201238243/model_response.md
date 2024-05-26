```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;
import org.bouncycastle.crypto.tls.TlsStreamCipher;

import java.io.ByteArrayInputStream;
import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;

public class ChachaDecoder implements TlsStreamCipher {

    private TlsCipher cipher;
    private InputStream input;
    private OutputStream output;
    private int limit;

    public ChachaDecoder(TlsCipher cipher, InputStream input, OutputStream output) {
        this.cipher = cipher;
        this.input = input;
        this.output = output;
    }

    @Override
    public void init(TlsContext context, int readAhead) throws IOException {
        this.cipher.init(context, false);
        this.limit = readAhead;
    }

    @Override
    public byte[] read() throws IOException {
        int len = Math.min(limit, input.available());
        byte[] buf = new byte[len];
        int off = 0;
        while (len > 0) {
            int read = input.read(buf, off, len);
            if (read < 0) {
                throw new TlsFatalAlert(AlertDescription.unexpected_message);
            }
            off += read;
            len -= read;
        }
        cipher.update(buf, 0, buf.length, buf, 0);
        return buf;
    }

    @Override
    public void write(byte[] buf, int off, int len) throws IOException {
        cipher.update(buf, off, len, buf, off);
        output.write(buf, off, len);
    }

    @Override
    public int getPlaintextLimit(int ciphertextLimit) {
        return ciphertextLimit;
    }

    @Override
    public byte[] getNonce() {
        return cipher.getNonce();
    }

    @Override
    public int getOutputSize(int inputLength) {
        return inputLength;
    }

    @Override
    public int getCiphertextSize(int inputLength) {
        return inputLength;
    }

    @Override
    public void reset() {
        cipher.reset();
    }

    @Override
    public void close() throws IOException {
        input.close();
        output.close();
    }
}
```