Here is a proposed patch for the failing client code:
```java
import javax.crypto.Cipher;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

public class ChachaDecoder {
    public byte[] decode(byte[] data, byte[] key, byte[] iv) {
        try {
            Cipher cipher = Cipher.getInstance("ChaCha20-Poly1305");
            SecretKeySpec keySpec = new SecretKeySpec(key, "ChaCha20");
            IvParameterSpec ivSpec = new IvParameterSpec(iv);
            cipher.init(Cipher.DECRYPT_MODE, keySpec, ivSpec);
            return cipher.doFinal(data);
        } catch (Exception e) {
            throw new RuntimeException(e);
        }
    }
}
```
It appears that the original code was trying to use the ChaCha20 cipher, but the `Cipher` class does not have a static method for instantiating a ChaCha20 cipher directly. Instead, we need to use the `Cipher.getInstance()` method to get an instance of the ChaCha20 cipher, and then initialize it with the key and IV as before.

Note that this patch assumes that the JCE Unlimited Strength Jurisdiction Policy Files have been installed. If not, the `Cipher.getInstance()` method may throw a `NoSuchAlgorithmException`.