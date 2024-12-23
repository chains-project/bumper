```java
import org.bouncycastle.util.Arrays;

import java.io.IOException;
import java.nio.ByteBuffer;

public class ChachaDecoder {

    private final ChachaCipher cipher;

    public ChachaDecoder(ChachaCipher cipher) {
        this.cipher = cipher;
    }

    public byte[] decode(byte[] in, int inOff, int len) throws IOException {
        if (len < 16) {
            throw new IOException("ChaChaDecoder: input too short");
        }

        byte[] output = new byte[len - 16];
        cipher.init(false, in, inOff);
        cipher.processBytes(in, inOff + 16, len - 16, output, 0);
        return output;
    }

    public byte[] decode(ByteBuffer in) throws IOException {
        byte[] input = new byte[in.remaining()];
        in.get(input);
        return decode(input, 0, input.length);
    }
}
```