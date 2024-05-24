```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private TextEncryptor textEncryptor;

    public GeoStoreDigestPasswordEncoder(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return textEncryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encodedPassword.equals(textEncryptor.encrypt(rawPassword.toString()));
    }

    public static void main(String[] args) {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        GeoStoreDigestPasswordEncoder passwordEncoder = new GeoStoreDigestPasswordEncoder(encryptor);
        // use passwordEncoder
    }
}
```