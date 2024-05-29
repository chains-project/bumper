Here's a proposed patch that replaces the failing client code:
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
In this patch, we replace the `PasswordEncoder` from `org.jasypt.spring.security` with `BasicPasswordEncryptor` from `org.jasypt.util.password`. The `encode` and `matches` methods are updated accordingly to use the new `BasicPasswordEncryptor` class.