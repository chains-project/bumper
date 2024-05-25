```java
import org.bouncycastle.crypto.tls.TlsCipher;
import org.bouncycastle.crypto.tls.TlsContext;

import javax.crypto.spec.SecretKeySpec;
import java.io.IOException;

public class ChachaDecoder {

    private final TlsCipher cipher;
    private final TlsContext context;

    public ChachaDecoder(TlsCipher cipher, TlsContext context) {
        this.cipher = cipher;
        this.context = context;
    }

    public byte[] decode(byte[] input, int offset, int len) throws IOException {
        byte[] output = new byte[len];
        cipher.decrypt(input, offset, len, output, 0);
        return output;
    }
}
```