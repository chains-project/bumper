```java
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class GeoStoreDigestPasswordEncoder extends BCryptPasswordEncoder {

    public GeoStoreDigestPasswordEncoder() {
        super();
    }

    public GeoStoreDigestPasswordEncoder(int strength) {
        super(strength);
    }

    public GeoStoreDigestPasswordEncoder(int strength, int rounds) {
        super(strength, rounds);
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return super.encode(rawPassword);
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return super.matches(rawPassword, encodedPassword);
    }
}
```