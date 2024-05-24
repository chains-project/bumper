```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public ChachaDecoder() {
    }

    public void decode(byte[] in, int inOff, int len) {
        if (len < 16) {
            throw new TlsFatalAlert(47);
        } else {
            int counter = in[inOff] & 255 | (in[inOff + 1] & 255) << 8 | (in[inOff + 2] & 255) << 16 | (in[inOff + 3] & 255) << 24;
            int nonce = in[inOff + 4] & 255 | (in[inOff + 5] & 255) << 8 | (in[inOff + 6] & 255) << 16 | (in[inOff + 7] & 255) << 24;
            int key = in[inOff + 8] & 255 | (in[inOff + 9] & 255) << 8 | (in[inOff + 10] & 255) << 16 | (in[inOff + 11] & 255) << 24;
            int streamPos = in[inOff + 12] & 255 | (in[inOff + 13] & 255) << 8 | (in[inOff + 14] & 255) << 16 | (in[inOff + 15] & 255) << 24;
            byte[] keyBytes = new byte[32];
            keyBytes[0] = (byte)(key >>> 24);
            keyBytes[1] = (byte)(key >>> 16);
            keyBytes[2] = (byte)(key >>> 8);
            keyBytes[3] = (byte)key;
            keyBytes[4] = (byte)(key >>> 24);
            keyBytes[5] = (byte)(key >>> 16);
            keyBytes[6] = (byte)(key >>> 8);
            keyBytes[7] = (byte)key;
            keyBytes[8] = (byte)(key >>> 24);
            keyBytes[9] = (byte)(key >>> 16);
            keyBytes[10] = (byte)(key >>> 8);
            keyBytes[11] = (byte)key;
            keyBytes[12] = (byte)(key >>> 24);
            keyBytes[13] = (byte)(key >>> 16);
            keyBytes[14] = (byte)(key >>> 8);
            keyBytes[15] = (byte)key;
            byte[] nonceBytes = new byte[12];
            nonceBytes[0] = (byte)(nonce >>> 24);
            nonceBytes[1] = (byte)(nonce >>> 16);
            nonceBytes[2] = (byte)(nonce >>> 8);
            nonceBytes[3] = (byte)nonce;
            nonceBytes[4] = (byte)(counter >>> 24);
            nonceBytes[5] = (byte)(counter >>> 16);
            nonceBytes[6] = (byte)(counter >>> 8);
            nonceBytes[7] = (byte)counter;
            nonceBytes[8] = 0;
            nonceBytes[9] = 0;
            nonceBytes[10] = 0;
            nonceBytes[11] = 0;
            byte[] streamPosBytes = new byte[4];
            streamPosBytes[0] = (byte)(streamPos >>> 24);
            streamPosBytes[1] = (byte)(streamPos >>> 16);
            streamPosBytes[2] = (byte)(streamPos >>> 8);
            streamPosBytes[3] = (byte)streamPos;
            byte[] aead = new byte[in.length - inOff - 16];
            System.arraycopy(in, inOff + 16, aead, 0, aead.length);
            byte[] aad = new byte[0];
            byte[] mac = new byte[0];
            byte[] plaintext = new byte[0];
            try {
                plaintext = Chacha20Poly1305.decrypt(keyBytes, nonceBytes, streamPosBytes, aad, aead, mac);
            } catch (Exception var17) {
                throw new TlsFatalAlert(47);
            }

            System.arraycopy(plaintext, 0, in, inOff, plaintext.length);
        }
    }
}
```