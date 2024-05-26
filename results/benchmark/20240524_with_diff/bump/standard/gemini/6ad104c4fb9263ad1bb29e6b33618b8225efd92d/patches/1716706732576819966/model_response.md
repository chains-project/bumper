```java
import org.bouncycastle.util.Arrays;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {
    public byte[] decode(byte[] ciphertext, byte[] key, byte[] nonce) {
        byte[] plaintext = new byte[ciphertext.length];
        Arrays.fill(plaintext, (byte) 0);
        chacha20(key, nonce, 0, ciphertext, 0, plaintext, 0, ciphertext.length);
        return plaintext;
    }

    private static void chacha20(byte[] key, byte[] nonce, int counter, byte[] in, int inOff, byte[] out, int outOff, int len) {
        // ChaCha20 encryption/decryption
    }
}
```