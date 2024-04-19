```java
import org.bouncycastle.crypto.tls.AlertDescription;
import org.bouncycastle.crypto.tls.TlsCipher;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final TlsCipher cipher;

    public ChachaDecoder(TlsCipher cipher) {
        this.cipher = cipher;
    }

    public byte[] decode(ByteBuffer in, int len) throws IOException {
        byte[] data = new byte[len];
        in.get(data);
        cipher.decrypt(data, 0, len);
        return data;
    }
}
```