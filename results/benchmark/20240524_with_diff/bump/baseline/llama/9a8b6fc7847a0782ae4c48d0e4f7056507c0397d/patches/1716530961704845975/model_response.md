```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private TextEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
    }

    public String encodePassword(String rawPass, Object salt) {
        return encryptor.encrypt(rawPass);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return encryptor.decrypt(encPass).equals(rawPass);
    }
}
```