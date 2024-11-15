```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;
import org.bouncycastle.crypto.tls.TlsCredentials;
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.io.OutputStream;

/**
 * A ChaCha20Poly1305 cipher for TLS 1.3.
 */
public class ChachaDecoder implements TlsCipher {

    private TlsContext context;
    private TlsCredentials credentials;

    public ChachaDecoder(TlsContext context, TlsCredentials credentials) {
        this.context = context;
        this.credentials = credentials;
    }

    public int getCiphertextDecodeLimit(int plaintextLimit) {
        return plaintextLimit;
    }

    public int getCiphertextEncodeLimit(int plaintextLimit) {
        return plaintextLimit;
    }

    public void init(TlsContext context, int receiveMode) throws IOException {
        this.context = context;
    }

    public byte[] decodeCiphertext(int type, byte[] ciphertext, int offset, int len) throws IOException {
        if (type != TlsProtocol.ALERT) {
            throw new TlsFatalAlert(AlertDescription.illegal_parameter);
        }

        if (len < 2) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int alertLevel = ciphertext[offset];
        int alertDescription = ciphertext[offset + 1];

        if (alertLevel != AlertDescription.warning && alertLevel != AlertDescription.fatal) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        if (len > 2) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        return new byte[]{ (byte) alertLevel, (byte) alertDescription };
    }

    public byte[] encodePlaintext(int type, byte[] plaintext, int offset, int len) throws IOException {
        if (type != TlsProtocol.ALERT) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }

        if (len < 2) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }

        int alertLevel = plaintext[offset];
        int alertDescription = plaintext[offset + 1];

        if (alertLevel != AlertDescription.warning && alertLevel != AlertDescription.fatal) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }

        if (len > 2) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }

        return new byte[]{ (byte) alertLevel, (byte) alertDescription };
    }

    public void exportKeyingMaterial(OutputStream stream, String asciiLabel, byte[] context_value, int length)
        throws IOException {
        TlsUtils.exportKeyingMaterial(context, asciiLabel, context_value, length, stream);
    }
}
```