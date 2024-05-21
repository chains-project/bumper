```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor implements PasswordEncoder {

    @Override
    public String encode(CharSequence rawPassword) {
        return encrypt(rawPassword);
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return checkPassword(rawPassword, encodedPassword);
    }

    public GeoStorePBEPasswordEncoder(String password, String salt) {
        setPassword(password);
        setSalt(salt);
    }
}
```