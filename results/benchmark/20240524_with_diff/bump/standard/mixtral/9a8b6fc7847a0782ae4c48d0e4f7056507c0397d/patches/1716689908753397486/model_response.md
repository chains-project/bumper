Here'Fully qualified code to replace the entire failing client code:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncrypts
```