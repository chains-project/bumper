Here's a proposed patch for the given client code:
```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();

    public String encode(String rawPass) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean matches(String rawPass, String encodedPass) {
        return passwordEncryptor.checkPassword(rawPass, encodedPass);
    }
}
```
In this patch, I replaced the `PasswordEncoder` from `org.jasypt.spring.security` package with `StrongPasswordEncryptor` from `org.jasypt.util.password` package. This way, the code no longer depends on the `org.jasypt.spring.security` package, which should solve the error.