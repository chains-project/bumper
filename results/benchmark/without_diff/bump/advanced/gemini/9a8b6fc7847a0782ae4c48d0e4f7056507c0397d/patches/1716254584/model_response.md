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

    public GeoStorePBEPasswordEncoder(boolean encodeHashAsBase64) {
        super(encodeHashAsBase64);
    }

    public GeoStorePBEPasswordEncoder(int strength, int rounds, boolean encodeHashAsBase64) {
        super(strength, rounds, encodeHashAsBase64);
    }

    public String encode(CharSequence rawPassword) {
        return super.encode(rawPassword);
    }

    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return super.matches(rawPassword, encodedPassword);
    }

}
```