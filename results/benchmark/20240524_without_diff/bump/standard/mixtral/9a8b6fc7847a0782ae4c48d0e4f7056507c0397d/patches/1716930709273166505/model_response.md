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

This patch replaces the `PasswordEncoder` class from `org.jasypt.spring.security` with the `BasicPasswordEncryptor` class from `org.jasypt.util.password`. This class provides similar functionality for encoding and checking passwords. The method signatures have not been changed, but the implementation has been updated to use the new class.