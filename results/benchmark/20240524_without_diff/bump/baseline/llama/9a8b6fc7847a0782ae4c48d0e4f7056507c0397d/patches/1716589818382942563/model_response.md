```java
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {
    @Override
    public String encode(CharSequence rawPassword) {
        // implement your custom encoding logic here
        return null;
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        // implement your custom matching logic here
        return false;
    }
}
```