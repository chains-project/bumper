```java
import org.bouncycastle.util.Arrays;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, byte[] out, int outOff, int len) {
        if (len < 0) {
            throw new IllegalArgumentException("len < 0");
        }
        if (len > in.length - inOff) {
            throw new IllegalArgumentException("len > in.length - inOff");
        }
        if (len > out.length - outOff) {
            throw new IllegalArgumentException("len > out.length - outOff");
        }
        byte[] tmp = new byte[len];
        System.arraycopy(in, inOff, tmp, 0, len);
        Arrays.fill(tmp, 0, len, (byte) 0);
        System.arraycopy(tmp, 0, out, outOff, len);
    }
}
```