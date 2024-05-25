```java
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class GeoStoreDigestPasswordEncoder {
    public PasswordEncoder getPasswordEncoder() {
        return new BCryptPasswordEncoder();
    }
}
```