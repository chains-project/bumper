```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private TextEncryptor textEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        textEncryptor = encryptor;
    }

    public String encodePassword(String rawPassword, Object salt) {
        return textEncryptor.encrypt(rawPassword);
    }

    public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
        String encodedPassword = textEncryptor.encrypt(rawPassword);
        return encodedPassword.equals(encPassword);
    }
}
```