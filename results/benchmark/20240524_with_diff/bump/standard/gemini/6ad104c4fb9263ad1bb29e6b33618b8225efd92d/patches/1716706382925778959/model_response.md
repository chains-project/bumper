```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public ChachaDecoder() {
    }

    public void decode(byte[] input, int inOff, int len) {
        if (len < 12) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }
        int nonce = input[inOff] & 0xFF;
        nonce |= (input[inOff + 1] & 0xFF) << 8;
        nonce |= (input[inOff + 2] & 0xFF) << 16;
        nonce |= (input[inOff + 3] & 0xFF) << 24;
        int counter = input[inOff + 4] & 0xFF;
        counter |= (input[inOff + 5] & 0xFF) << 8;
        counter |= (input[inOff + 6] & 0xFF) << 16;
        counter |= (input[inOff + 7] & 0xFF) << 24;
        int keyStreamLen = input[inOff + 8] & 0xFF;
        keyStreamLen |= (input[inOff + 9] & 0xFF) << 8;
        keyStreamLen |= (input[inOff + 10] & 0xFF) << 16;
        keyStreamLen |= (input[inOff + 11] & 0xFF) << 24;
        if (keyStreamLen != len - 12) {
            throw new TlsFatalAlert(TlsFatalAlert.DECODE_ERROR);
        }
        byte[] keyStream = new byte[keyStreamLen];
        System.arraycopy(input, inOff + 12, keyStream, 0, keyStreamLen);
        // TODO: Decrypt the data using the key stream
    }
}
```