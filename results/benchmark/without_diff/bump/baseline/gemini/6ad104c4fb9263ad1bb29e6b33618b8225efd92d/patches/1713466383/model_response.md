```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 8) {
            throw new IllegalArgumentException("Input buffer too short");
        }
        int nonce = in[inOff] & 0xff | (in[inOff + 1] & 0xff) << 8 | (in[inOff + 2] & 0xff) << 16 | (in[inOff + 3] & 0xff) << 24;
        int counter = in[inOff + 4] & 0xff | (in[inOff + 5] & 0xff) << 8 | (in[inOff + 6] & 0xff) << 16 | (in[inOff + 7] & 0xff) << 24;
        byte[] key = new byte[32];
        System.arraycopy(in, inOff + 8, key, 0, 32);
        byte[] additionalData = new byte[0];
        byte[] plaintext = new byte[len - 8];
        System.arraycopy(in, inOff + 40, plaintext, 0, len - 8);
        //++
        int result = ChaCha.process(key, counter, nonce, plaintext, additionalData, out, outOff, plaintext.length);
        if (result < 0) {
            throw new TlsFatalAlert(AlertDescription.internal_error);
        }
    }
}
```