```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        // TODO Auto-generated method stub
        if (len < 12) {
            throw new IllegalArgumentException("Given data too short: " + len + " bytes");
        }

        int nonce = in[inOff] & 0xFF;
        nonce |= (in[inOff + 1] & 0xFF) << 8;
        nonce |= (in[inOff + 2] & 0xFF) << 16;
        nonce |= (in[inOff + 3] & 0xFF) << 24;

        int counter = in[inOff + 4] & 0xFF;
        counter |= (in[inOff + 5] & 0xFF) << 8;
        counter |= (in[inOff + 6] & 0xFF) << 16;
        counter |= (in[inOff + 7] & 0xFF) << 24;

        int keyStreamOff = inOff + 8;
        int keyStreamLen = len - 12;

        byte[] keyStream = new byte[keyStreamLen];
        System.arraycopy(in, keyStreamOff, keyStream, 0, keyStreamLen);

        // TODO: Implement ChaCha20 decryption
        // Decrypt the key stream using the nonce and counter
        // Copy the decrypted key stream to the output buffer

        System.arraycopy(keyStream, 0, out, outOff, keyStreamLen);
    }

}
```