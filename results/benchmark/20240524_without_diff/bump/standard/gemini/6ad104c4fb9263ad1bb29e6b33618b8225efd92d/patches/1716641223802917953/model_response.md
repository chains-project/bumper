```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public byte[] decode(byte[] data, int offset, int len) {
        if (data == null) {
            throw new IllegalArgumentException("Data cannot be null");
        }
        if (offset < 0 || offset >= data.length) {
            throw new IllegalArgumentException("Invalid offset");
        }
        if (len < 0 || offset + len > data.length) {
            throw new IllegalArgumentException("Invalid length");
        }

        byte[] result = new byte[len];
        System.arraycopy(data, offset, result, 0, len);
        return result;
    }
}
```