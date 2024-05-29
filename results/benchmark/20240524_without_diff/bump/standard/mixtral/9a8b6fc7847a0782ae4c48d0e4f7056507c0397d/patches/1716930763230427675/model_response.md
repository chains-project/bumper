Here's a proposed patch for the failing client code:
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
In this patch, I replaced the `PasswordEncoder` class from `org.jasypt.spring.security` package with `BasicPasswordEncryptor` class from `org.jasypt.util.password` package. This is because the `PasswordEncoder` class is no longer available in the `org.jasypt.spring.security` package. Instead, we can use `BasicPasswordEncryptor` to encrypt and check passwords.