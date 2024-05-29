Here's a proposed patch for the client code:
```java
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StrongTextEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        this.encryptor = new StrongTextEncryptor();
        this.encryptor.setAlgorithm("PBEWithMD5AndTripleDES");
    }

    public String encode(String rawPass) {
        return this.encryptor.encrypt(rawPass);
    }

    public boolean matches(String rawPass, String encodedPass) {
        return encodedPass.equals(encryptor.encrypt(rawPass));
    }
}
```
This patch replaces the use of the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package with the `StrongTextEncryptor` class from the `org.jasypt.util.text` package. The `StrongTextEncryptor` class provides similar functionality to the `PBEPasswordEncoder` class, allowing for the encryption and decryption of passwords.

Note that the `setAlgorithm` method is used to set the encryption algorithm to `PBEWithMD5AndTripleDES`, which is the default algorithm used by the `PBEPasswordEncoder` class. Additionally, the `matches` method has been updated to use the `encrypt` method of the `StrongTextEncryptor` class to compare the raw password with the encoded password.