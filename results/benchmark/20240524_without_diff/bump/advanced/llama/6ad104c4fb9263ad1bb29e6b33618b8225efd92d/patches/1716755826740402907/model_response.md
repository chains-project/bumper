```java
import java.security.Security;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class ChachaDecoder {
    public void decode(byte[] key, byte[] nonce, byte[] ciphertext) throws Exception {
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        Cipher cipher = Cipher.getInstance("ChaCha20", "BC");
        SecretKeySpec keySpec = new SecretKeySpec(key, "ChaCha20");
        cipher.init(Cipher.DECRYPT_MODE, keySpec);
        byte[] plaintext = cipher.doFinal(ciphertext);
    }
}
```