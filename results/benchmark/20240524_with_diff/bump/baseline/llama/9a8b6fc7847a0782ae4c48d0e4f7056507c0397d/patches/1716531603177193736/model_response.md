```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private TextEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
    }

    public String encodePassword(String rawPassword, Object salt) {
        return encryptor.encrypt(rawPassword);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return encryptor.decrypt(encPass).equals(rawPass);
    }
}
```