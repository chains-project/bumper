```java
import org.bouncycastle.util.Arrays;
import org.bouncycastle.crypto.tls.TlsFatalAlert;

public class ChachaDecoder {

    public ChachaDecoder(byte[] key, byte[] iv) {
        // ...
    }

    public byte[] decode(byte[] ciphertext, int offset, int len) {
        byte[] plaintext = new byte[len];
        // ...
        return plaintext;
    }

    public static void main(String[] args) throws Exception {
        byte[] key = new byte[32];
        byte[] iv = new byte[12];
        ChachaDecoder decoder = new ChachaDecoder(key, iv);
        byte[] ciphertext = new byte[1024];
        byte[] plaintext = decoder.decode(ciphertext, 0, ciphertext.length);
        System.out.println(Arrays.toHexString(plaintext));
    }
}
```