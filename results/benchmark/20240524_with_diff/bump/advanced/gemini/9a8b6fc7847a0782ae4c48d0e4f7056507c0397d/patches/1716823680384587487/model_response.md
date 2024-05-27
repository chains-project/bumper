```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;

public class GeoStorePBEPasswordEncoder {

    private PasswordEncoder passwordEncoder;

    public GeoStorePBEPasswordEncoder() {
        passwordEncoder = new PasswordEncoder();
        passwordEncoder.setPasswordEncryptor(new StandardPBEStringEncryptor());
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncoder.encodePassword(password, salt);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return passwordEncoder.isPasswordValid(encodedPassword, rawPassword, salt);
    }
}
```