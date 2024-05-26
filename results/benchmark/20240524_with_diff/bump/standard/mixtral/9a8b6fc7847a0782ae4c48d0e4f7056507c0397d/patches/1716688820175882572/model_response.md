Here is the proposed patch for the failing client code:

```java
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import java.lang.String;

public class GeoStoreDigestPasswordEncoder {
    //...
    private PasswordEncryptor passwordEncryptor = new PasswordEncryptor();
    private TextEncryptor textEncryptor = new TextEncryptor();

    public String encodePassword(String rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encryptedPassword, String rawPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encryptedPassword);
    }

    //...
}
```

This patch replaces the usage of `org.jasypt.spring.security` package with `org.jasypt.util` package. The `PasswordEncoder` interface has been removed from the `org.jasypt.spring.security` package, so we are using `PasswordEncryptor` and `TextEncryptor` classes directly from `org.jasypt.util` package to encode and validate passwords.