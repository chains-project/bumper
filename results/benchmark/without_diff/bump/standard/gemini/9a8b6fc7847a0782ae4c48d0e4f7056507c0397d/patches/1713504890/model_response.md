```java
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends BCryptPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
    }

    public GeoStorePBEPasswordEncoder(int strength) {
        super(strength);
    }

    public GeoStorePBEPasswordEncoder(int strength, int rounds) {
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