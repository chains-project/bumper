```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private final PBEStringEncryptor pbeStringEncryptor;

    public GeoStoreDigestPasswordEncoder(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return pbeStringEncryptor.encrypt(rawPassword);
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return pbeStringEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```