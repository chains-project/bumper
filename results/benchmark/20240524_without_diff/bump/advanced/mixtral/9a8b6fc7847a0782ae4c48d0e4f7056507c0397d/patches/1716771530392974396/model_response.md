Here is the proposed patch:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();

    public String encode(String rawPass) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean matches(String rawPass, String encodedPass) {
        return passwordEncryptor.checkPassword(rawPass, encodedPass);
    }
}
```

This patch replaces the `PasswordEncoder` interface from `org.jasypt.spring.security` with the `BasicPasswordEncryptor` class from `org.jasypt.util.password`. The `encode` and `matches` methods have been updated to use the new class.