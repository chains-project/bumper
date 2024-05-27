```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsProtocol;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    public static byte[] decode(ByteBuffer in, int length) throws IOException {
        if (length < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        byte[] iv = new byte[8];
        in.get(iv);

        byte[] key = new byte[8];
        in.get(key);

        byte[] data = new byte[length - 16];
        in.get(data);

        return Chacha20Poly1305.decrypt(key, iv, data);
    }
}
```