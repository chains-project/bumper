Here is a possible patch for the failing client code:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder {

    private final PasswordEncoder passwordEncoder = new PasswordEncoder() {

        private final BasicPasswordEncryptor basicPasswordEncryptor = new BasicPasswordEncrypts
```