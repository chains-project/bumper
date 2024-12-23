```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int nonce = in[inOff] & 0xFF
                | (in[inOff + 1] & 0xFF) << 8
                | (in[inOff + 2] & 0xFF) << 16
                | (in[inOff + 3] & 0xFF) << 24;

        int counter = in[inOff + 4] & 0xFF
                | (in[inOff + 5] & 0xFF) << 8
                | (in[inOff + 6] & 0xFF) << 16
                | (in[inOff + 7] & 0xFF) << 24;

        byte[] key = new byte[32];
        System.arraycopy(in, inOff + 8, key, 0, 32);

        byte[] block = new byte[64];
        System.arraycopy(in, inOff + 40, block, 0, 64);

        Chacha20Engine chacha = new Chacha20Engine();
        chacha.init(key, counter, nonce);
        chacha.processBytes(block, 0, block.length, out, outOff);
    }
}
```