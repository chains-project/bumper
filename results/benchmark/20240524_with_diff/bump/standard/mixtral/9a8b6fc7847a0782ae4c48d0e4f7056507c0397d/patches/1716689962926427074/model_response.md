Here is a possible patch for the failing client code:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.authentication.encoding.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncrypts
```