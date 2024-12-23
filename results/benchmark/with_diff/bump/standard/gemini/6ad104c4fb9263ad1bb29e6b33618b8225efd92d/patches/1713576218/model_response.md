```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 16) {
            throw new IllegalArgumentException("Input must be at least 16 bytes long");
        }

        int keyStreamPos = 0;
        for (int i = 0; i < len; i++) {
            out[outOff + i] = (byte) (in[inOff + i] ^ out[keyStreamPos]);
            keyStreamPos++;
            if (keyStreamPos == 64) {
                keyStreamPos = 0;
            }
        }
    }

    public void decode(byte[] in, int inOff, int len) {
        decode(in, inOff, len, in, inOff);
    }

    public static void main(String[] args) {
        ChachaDecoder decoder = new ChachaDecoder();
        byte[] in = new byte[16];
        byte[] out = new byte[16];
        decoder.decode(in, 0, 16, out, 0);
        System.out.println(new String(out));
    }
}
```