```java
import org.springframework.security.crypto.password.PBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder {
    public PBEPasswordEncoder getPasswordEncoder() {
        return new PBEPasswordEncoder();
    }
}
```