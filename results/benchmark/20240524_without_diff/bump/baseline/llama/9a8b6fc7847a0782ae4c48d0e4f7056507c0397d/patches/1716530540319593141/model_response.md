```java
import org.jasypt.spring.security.PasswordEncoder;

public class GeoStorePBEPasswordEncoder extends PasswordEncoder {

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return super.encodePassword(rawPass, salt);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return super.isPasswordValid(encPass, rawPass, salt);
    }
}
```