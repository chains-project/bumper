```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 16) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int nonce = in[inOff] & 0xFF | (in[inOff + 1] & 0xFF) << 8 | (in[inOff + 2] & 0xFF) << 16 | (in[inOff + 3] & 0xFF) << 24;
        int counter = in[inOff + 4] & 0xFF | (in[inOff + 5] & 0xFF) << 8 | (in[inOff + 6] & 0xFF) << 16 | (in[inOff + 7] & 0xFF) << 24;

        byte[] key = new byte[32];
        System.arraycopy(in, inOff + 8, key, 0, 32);

        byte[] block = new byte[64];
        System.arraycopy(in, inOff + 40, block, 0, 64);

        byte[] stream = new byte[len - 16];
        System.arraycopy(in, inOff + 16, stream, 0, len - 16);

        // Decrypt the stream
        for (int i = 0; i < stream.length; i += 64) {
            int n = i / 64;
            int c = counter + n;

            byte[] nonceAndCounter = new byte[12];
            System.arraycopy(key, 0, nonceAndCounter, 0, 4);
            nonceAndCounter[4] = (byte) (nonce >> 24);
            nonceAndCounter[5] = (byte) (nonce >> 16);
            nonceAndCounter[6] = (byte) (nonce >> 8);
            nonceAndCounter[7] = (byte) nonce;
            nonceAndCounter[8] = (byte) (c >> 24);
            nonceAndCounter[9] = (byte) (c >> 16);
            nonceAndCounter[10] = (byte) (c >> 8);
            nonceAndCounter[11] = (byte) c;

            byte[] keyStream = new byte[64];
            new ChachaEngine().processBytes(nonceAndCounter, 0, nonceAndCounter.length, keyStream, 0);

            for (int j = 0; j < 64; j++) {
                stream[i + j] ^= keyStream[j];
            }
        }

        // Copy the decrypted stream to the output buffer
        System.arraycopy(stream, 0, out, outOff, stream.length);
    }
}
```