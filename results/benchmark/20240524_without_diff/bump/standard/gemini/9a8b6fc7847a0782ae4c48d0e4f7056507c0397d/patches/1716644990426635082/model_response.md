```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        this.passwordEncryptor = new StrongPasswordEncryptor();
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```