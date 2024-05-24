```java
import org.jasypt.encryption.pbe.PBEEncryptor;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

@Component
public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private final PBEEncryptor encryptor;
    private final PasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("my-secret-password");
        passwordEncryptor = new PasswordEncryptor();
        passwordEncryptor.setPassword("my-secret-password");
    }

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