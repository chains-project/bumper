```java
import org.bouncycastle.crypto.tls.AlertDescription;

import java.io.IOException;

public class ChachaDecoder {

    private final TlsCipher cipher;

    public ChachaDecoder(TlsCipher cipher) {
        this.cipher = cipher;
    }

    public byte[] decode(byte[] in, int inOff, int len) throws IOException {
        byte[] out = new byte[len];
        cipher.decodeCiphertext(in, inOff, len, out, 0);
        return out;
    }

    public void close() throws IOException {
        cipher.close();
    }
}
```