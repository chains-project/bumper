```java
import org.springframework.security.crypto.password.PBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends PBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder(String salt) {
        super(salt);
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