```java
import org.jasypt.encryption.pbe.PBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends PBEPasswordEncoder {

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