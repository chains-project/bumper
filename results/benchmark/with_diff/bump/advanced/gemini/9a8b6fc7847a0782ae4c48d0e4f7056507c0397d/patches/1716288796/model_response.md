```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("geosolutions");
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```