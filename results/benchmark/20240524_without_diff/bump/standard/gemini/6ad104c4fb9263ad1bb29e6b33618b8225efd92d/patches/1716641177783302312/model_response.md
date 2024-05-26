```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;

public class ChachaDecoder {

    private final TlsProtocol tlsProtocol;

    public ChachaDecoder(TlsProtocol tlsProtocol) {
        this.tlsProtocol = tlsProtocol;
    }

    public byte[] decode(byte[] in, int len) throws IOException {
        if (in == null) {
            throw new IllegalArgumentException("Input cannot be null");
        }
        if (len < 0) {
            throw new IllegalArgumentException("Length cannot be negative");
        }
        if (len > in.length) {
            throw new IllegalArgumentException("Length cannot be greater than input length");
        }

        // Check if the length is valid for the current protocol version.
        if (len > tlsProtocol.getMaxFragmentLength()) {
            throw new TlsFatalAlert(AlertDescription.record_overflow);
        }

        // Create a new byte array to hold the decoded data.
        byte[] out = new byte[len];

        // Copy the input data into the output array.
        System.arraycopy(in, 0, out, 0, len);

        return out;
    }
}
```