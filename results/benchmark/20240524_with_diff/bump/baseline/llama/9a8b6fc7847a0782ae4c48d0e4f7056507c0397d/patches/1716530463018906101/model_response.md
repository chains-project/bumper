```java
import org.jasypt.spring.security.PasswordEncoder;

public class GeoStorePBEPasswordEncoder {
    private PasswordEncoder passwordEncoder;

    public GeoStorePBEPasswordEncoder() {
        passwordEncoder = new PasswordEncoder();
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return passwordEncoder.encodePassword(rawPass, salt);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncoder.isPasswordValid(encPass, rawPass, salt);
    }
}
```