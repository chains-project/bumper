```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {
    public void decode(byte[] in, int inOff, int len) {
        if (len < 1) {
            throw new IllegalArgumentException("Given plaintext length is too short: " + len);
        }

        int encLen = len - 1;
        byte[] encData = new byte[encLen];
        System.arraycopy(in, inOff + 1, encData, 0, encLen);

        byte poly = in[inOff];

        int c = 0;
        for (int i = 0; i < encLen; i++) {
            c ^= encData[i];
        }

        if (c != poly) {
            throw new IllegalArgumentException("Given plaintext is not authentic");
        }
    }
}
```