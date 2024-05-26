Here is a possible patch for the failing client code:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private BasicPasswordEncryptor encryptor = new BasicPasswordEncryptor();

    public String encode(String rawPassword) {
        return encryptor.encryptPassword(rawPassword);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```
In this patch, we have replaced the `PasswordEncoder` interface from `org.jasypt.spring.security` with the `BasicPasswordEncryptor` class from `org.jasypt.util.password`. This allows us to encode and check passwords using the same methods as before, but without relying on the Spring-specific `PasswordEncoder` interface.

Note that this patch assumes that the original code was using the `PasswordEncoder` interface from `org.jasypt.spring.security` only for encoding and checking passwords, and not for any other Spring-specific functionality. If the original code was using any other methods from `org.jasypt.spring.security`, those may need to be replaced or removed as well.