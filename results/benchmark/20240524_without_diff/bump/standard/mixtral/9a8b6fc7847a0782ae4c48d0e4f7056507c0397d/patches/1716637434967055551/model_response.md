Here's the proposed patch:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();

    public String encode(String rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```
Note: This patch replaces the `PasswordEncoder` from `org.jasypt.spring.security` package with `BasicPasswordEncryptor` from `org.jasypt.util.password` package. The `encode` and `matches` methods are updated accordingly.