Here's the patched method:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    // ...

    public GeoStoreDigestPasswordEncoder() {
        this.passwordEncryptor = new BasicPasswordEncryptor();
    }

    // ...
}
```
I replaced the `org.jasypt.spring.security.PasswordEncoder` with `org.jasypt.util.password.BasicPasswordEncryptor` as a drop-in replacement. This change should resolve the compilation error.