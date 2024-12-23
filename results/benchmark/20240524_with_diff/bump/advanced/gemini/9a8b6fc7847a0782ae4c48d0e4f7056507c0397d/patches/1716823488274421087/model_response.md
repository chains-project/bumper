```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private final PBEStringEncryptor encryptor;
    private final PasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder(PBEStringEncryptor encryptor, PasswordEncryptor passwordEncryptor) {
        this.encryptor = encryptor;
        this.passwordEncryptor = passwordEncryptor;
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encryptPassword(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```