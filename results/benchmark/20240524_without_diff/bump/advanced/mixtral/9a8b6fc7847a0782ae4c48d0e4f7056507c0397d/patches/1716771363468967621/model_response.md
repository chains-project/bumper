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
In this patch, I replaced the `PasswordEncoder` class from `org.jasypt.spring.security` with the `BasicPasswordEncryptor` class from `org.jasypt.util.password`. The `BasicPasswordEncryptor` class provides similar functionality to the `PasswordEncoder` interface, so the existing code can still work with minimal modifications.

Note that the `PasswordEncoder` interface from `org.jasypt.spring.security` has been deprecated and replaced with the `PasswordEncryptor` interface from `org.jasypt.util.password`. Therefore, it's recommended to use the `BasicPasswordEncryptor` class instead of the deprecated `PasswordEncoder` interface.