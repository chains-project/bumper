Here's the proposed patch:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();

    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }

    public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword.toString());
    }
}
```

Note that I replaced the `PasswordEncoder` from `org.jasypt.spring.security` with `BasicPasswordEncryptor` from `org.jasypt.util.password`. The `matches` and `encode` methods were updated accordingly.