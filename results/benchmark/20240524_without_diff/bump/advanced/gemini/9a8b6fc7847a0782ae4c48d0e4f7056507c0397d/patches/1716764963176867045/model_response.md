```java
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    @Autowired
    private PasswordEncryptor passwordEncryptor;

    @Override
    public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```