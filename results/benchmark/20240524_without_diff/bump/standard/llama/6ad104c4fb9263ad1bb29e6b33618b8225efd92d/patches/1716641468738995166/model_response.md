```java
import java.security.Security;
import javax.crypto.Cipher;
import javax.crypto.spec.SecretKeySpec;

public class ChachaDecoder {
    public void decode() {
        Security.addProvider(new org.bouncycastle.jce.provider.BouncyCastleProvider());
        Cipher cipher = Cipher.getInstance("ChaCha20-Poly1305", "BC");
        SecretKeySpec key = new SecretKeySpec(new byte[32], "ChaCha20");
        cipher.init(Cipher.DECRYPT_MODE, key);
    }
}
```