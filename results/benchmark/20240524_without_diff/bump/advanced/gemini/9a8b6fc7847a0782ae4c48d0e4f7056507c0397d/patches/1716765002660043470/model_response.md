```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private BasicPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        this.passwordEncryptor = new BasicPasswordEncryptor();
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