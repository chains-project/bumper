```java
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public void decode(byte[] in, int inOff, int len) {
        if (len < 12) {
            throw new TlsFatalAlert(AlertDescription.decode_error);
        }

        int nonce = in[inOff] & 0xFF;
        int streamPos = in[inOff + 1] & 0xFF;
        int counter = in[inOff + 2] & 0xFF;
        int counterHi = in[inOff + 3] & 0xFF;
        int counterLo = in[inOff + 4] & 0xFF;
        int counterMid = in[inOff + 5] & 0xFF;

        byte[] key = new byte[32];
        System.arraycopy(in, inOff + 6, key, 0, 32);

        byte[] iv = new byte[12];
        System.arraycopy(in, inOff, iv, 0, 12);

        // ++ Cipher cipher = Cipher.getInstance("ChaCha20/None/NoPadding");
        // ++ cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(key, "ChaCha20"), new IvParameterSpec(iv));
        // ++ cipher.doFinal(in, inOff + 12, len - 12, out, outOff);
    }
}
```