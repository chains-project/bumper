```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimplePBEConfig;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

public class GeoStoreDigestPasswordEncoder {

    private final BCryptPasswordEncoder bCryptPasswordEncoder = new BCryptPasswordEncoder();

    public String encodePassword(String password, Object salt) {
        String encodedPassword = bCryptPasswordEncoder.encode(password);
        return encodedPassword;
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return bCryptPasswordEncoder.matches(rawPassword, encodedPassword);
    }
}
```