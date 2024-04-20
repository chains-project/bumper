```java
import org.bouncycastle.crypto.tls.AlertDescription;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len, byte[] out, int outOff) {
        if (len < 16) {
            throw new IllegalArgumentException("Input too short: " + len);
        }

        if (out.length < len) {
            throw new IllegalArgumentException("Output buffer too small: " + out.length);
        }

        byte[] nonce = new byte[12];
        System.arraycopy(in, inOff, nonce, 0, 12);

        byte[] key = new byte[32];
        System.arraycopy(in, inOff + 12, key, 0, 32);

        byte[] ciphertext = new byte[len - 16];
        System.arraycopy(in, inOff + 16, ciphertext, 0, len - 16);

        byte[] plaintext = new byte[len - 16];
        chacha20(key, nonce, 0, plaintext, ciphertext);

        System.arraycopy(plaintext, 0, out, outOff, len - 16);
    }

    private void chacha20(byte[] key, byte[] nonce, int counter, byte[] out, byte[] in) {
        int[] state = new int[16];
        int[] x = new int[4];
        int[] y = new int[4];

        state[0] = 0x61707865;
        state[1] = 0x3320646e;
        state[2] = 0x79622d32;
        state[3] = 0x6b206574;
        state[4] = key[0] | (key[1] << 8) | (key[2] << 16) | (key[3] << 24);
        state[5] = key[4] | (key[5] << 8) | (key[6] << 16) | (key[7] << 24);
        state[6] = key[8] | (key[9] << 8) | (key[10] << 16) | (key[11] << 24);
        state[7] = key[12] | (key[13] << 8) | (key[14] << 16) | (key[15] << 24);
        state[8] = key[16] | (key[17] << 8) | (key[18] << 16) | (key[19] << 24);
        state[9] = key[20] | (key[21] << 8) | (key[22] << 16) | (key[23] << 24);
        state[10] = key[24] | (key[25] << 8) | (key[26] << 16) | (key[27] << 24);
        state[11] = key[28] | (key[29] << 8) | (key[30] << 16) | (key[31] << 24);
        state[12] = nonce[0] | (nonce[1] << 8) | (nonce[2] << 16) | (nonce[3] << 24);
        state[13] = nonce[4] | (nonce[5] << 8) | (nonce[6] << 16) | (nonce[7] << 24);
        state[14] = counter | (counter << 8) | (counter << 16) | (counter << 24);
        state[15] = 0;

        for (int i = 0; i < 10; i++) {
            x[0] = state[0];
            x[1] = state[1];
            x[2] = state[2];
            x[3] = state[3];
            for (int j = 0; j < 4; j++) {
                x[j] += state[(j * 5) % 16];
                x[j] = (x[j] << 16) | (x[j] >>> 16);
                x[j] += state[(j * 5 + 1) % 16];
                x[j] = (x[j] << 12) | (x[j] >>> 20);
                x[j] += state[(j * 5 + 2) % 16];
                x[j] = (x[j] << 8) | (x[j] >>> 24);
                x[j] += state[(j * 5 + 3) % 16];
                x[j] = (x[j] << 7) | (x[j] >>> 25);
            }
            y[0] = x[0] + state[4];
            y[1] = x[1] + state[5];
            y[2] = x[2] + state[6];
            y[3] = x[3] + state[7];
            x[0] = state[8];
            x[1] = state[9];
            x[2] = state[10];
            x[3] = state[11];
            for (int j = 0; j < 4; j++) {
                x[j] += y[(j * 5) % 4];
                x[j] = (x[j] << 16) | (x[j] >>> 16);
                x[j] += y[(j * 5 + 1) % 4];
                x[j] = (x[j] << 12) | (x[j] >>> 20);
                x[j] += y[(j * 5 + 2) % 4];
                x[j] = (x[j] << 8) | (x[j] >>> 24);
                x[j] += y[(j * 5 + 3) % 4];
                x[j] = (x[j] << 7) | (x[j] >>> 25);
            }
            y[0] = x[0] + state[12];
            y[1] = x[1] + state[13];
            y[2] = x[2] + state[14];
            y[3] = x[3] + state[15];
            state[0] = state[0] + y[0];
            state[1] = state[1] + y[1];
            state[2] = state[2] + y[2];
            state[3] = state[3] + y[3];
            state[4] = state[4] + x[0];
            state[5] = state[5] + x[1];
            state[6] = state[6] + x[2];
            state[7] = state[7] + x[3];
            state[8] = state[8] + y[0];
            state[9] = state[9] + y[1];
            state[10] = state[10] + y[2];
            state[11] = state[11] + y[3];
            state[12] = state[12] + x[0];
            state[13] = state[13] + x[1];
            state[14] = state[14] + x[2];
            state[15] = state[15] + x[3];
        }

        state[0] += 0x61707865;
        state[1] += 0x3320646e;
        state[2] += 0x79622d32;
        state[3] += 0x6b206574;
        state[4] += key[0] | (key[1] << 8) | (key[2] << 16) | (key[3] << 24);
        state[5] += key[4] | (key[5] << 8) | (key[6] << 16) | (key[7] << 24);
        state[6] += key[8] | (key[9] << 8) | (key[10] << 16) | (key[11] << 24);
        state[7] += key[12] | (key[13] << 8) | (key[14] << 16) | (key[15] << 24);
        state[8] += key[16] | (key[17] << 8) | (key[18] << 16) | (key[19] << 24);
        state[9] += key[20] | (key[21] << 8) | (key[22] << 16) | (key[23] << 24);
        state[10] += key[24] | (key[25] << 8) | (key[26] << 16) | (key[27] << 24);
        state[11] += key[28] | (key[29] << 8) | (key[30] << 16) | (key[31] << 24);
        state[12] += nonce[0] | (nonce[1] << 8) | (nonce[2] << 16) | (nonce[3] << 24);
        state[13] += nonce[4] | (nonce[5] << 8) | (nonce[6] << 16) | (nonce[7] << 24);
        state[14] += counter | (counter << 8) | (counter << 16) | (counter << 24);

        for (int i = 0; i < 16; i++) {
            out[i * 4] = (byte) (state[i] & 0xff);
            out[i * 4 + 1] = (byte) ((state[i] >> 8) & 0xff);
            out[i * 4 + 2] = (byte) ((state[i] >> 16) & 0xff);
            out[i * 4 + 3] = (byte) (state[i] >> 24);
        }

        for (int i = 0; i < 16; i++) {
            state[i] = state[i] & 0xffffffffL;
        }

        for (int i = 0; i < in.length; i++) {
            out[i] = (byte) (out[i] ^ in[i]);
        }
    }
}
```