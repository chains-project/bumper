Here's the proposed patch for the failing method:
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
In this patch, I replaced the `PasswordEncoder` from `org.jasypt.spring.security` package with `BasicPasswordEncryptor` from `org.jasypt.util.password` package. The `encode` and `matches` methods were updated accordingly.