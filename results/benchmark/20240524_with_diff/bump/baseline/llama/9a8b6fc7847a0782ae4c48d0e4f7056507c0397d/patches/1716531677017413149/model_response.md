```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private TextEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return rawPassword.toString().equals(encryptor.decrypt(encodedPassword));
    }
}
```