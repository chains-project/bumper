```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();

    @Override
    public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```