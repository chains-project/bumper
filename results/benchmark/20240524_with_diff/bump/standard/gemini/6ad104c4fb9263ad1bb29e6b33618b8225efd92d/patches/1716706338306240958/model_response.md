```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 12) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int nonce = in[inOff] & 0xFF;
        int counter = (in[inOff + 1] & 0xFF) << 8 | (in[inOff + 2] & 0xFF);
        int keyStreamPos = inOff + 3;

        for (int i = 0; i < len - 12; i++) {
            out[outOff + i] = (byte) (in[keyStreamPos + i] ^ in[keyStreamPos + i + 4]);
        }
    }
}
```