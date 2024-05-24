```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
        // Check if the input is long enough for the ChaCha20 header.
        if (len < 12) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Extract the ChaCha20 header.
        int nonce = in[inOff] & 0xFF;
        nonce |= (in[inOff + 1] & 0xFF) << 8;
        nonce |= (in[inOff + 2] & 0xFF) << 16;
        nonce |= (in[inOff + 3] & 0xFF) << 24;
        int counter = in[inOff + 4] & 0xFF;
        counter |= (in[inOff + 5] & 0xFF) << 8;
        int streamPos = in[inOff + 6] & 0xFF;
        streamPos |= (in[inOff + 7] & 0xFF) << 8;
        int streamLen = in[inOff + 8] & 0xFF;
        streamLen |= (in[inOff + 9] & 0xFF) << 8;
        int key = in[inOff + 10] & 0xFF;
        key |= (in[inOff + 11] & 0xFF) << 8;

        // Check if the input is long enough for the ChaCha20 payload.
        if (len < 12 + streamLen) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        // Create a ChaCha20 cipher.
        ChaCha20 cipher = new ChaCha20(key, nonce, counter, streamPos);

        // Decrypt the payload.
        cipher.processBytes(in, inOff + 12, streamLen, in, inOff + 12);
    }
}
```