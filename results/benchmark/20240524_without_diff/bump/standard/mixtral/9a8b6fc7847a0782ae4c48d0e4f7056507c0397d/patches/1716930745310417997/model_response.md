Here's the proposed patch:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private BasicPasswordEncryptor encryptor = new BasicPasswordEncryptor();

    public String encode(String rawPass) {
        return encryptor.encryptPassword(rawPass);
    }

    public boolean matches(String encPass, String rawPass) {
        return encryptor.checkPassword(rawPass, encPass);
    }
}
```
Note that I replaced the `PasswordEncoder` from `org.jasypt.spring.security` package with `BasicPasswordEncryptor` from `org.jasypt.util.password` package, which provides similar functionality.