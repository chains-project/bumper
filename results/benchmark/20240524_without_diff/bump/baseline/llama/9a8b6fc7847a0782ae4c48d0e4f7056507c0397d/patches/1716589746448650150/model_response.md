```java
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {
    @Override
    public String encode(CharSequence rawPassword) {
        // implementation
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        // implementation
    }
}
```