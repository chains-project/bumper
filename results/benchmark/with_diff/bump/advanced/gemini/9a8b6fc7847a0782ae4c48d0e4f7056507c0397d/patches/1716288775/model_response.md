```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;

public class GeoStorePBEPasswordEncoder extends PasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder(StandardPBEStringEncryptor encryptor) {
        this.encryptor = encryptor;
    }

    @Override
    public String encodePassword(String rawPassword, Object salt) {
        return encryptor.encrypt(rawPassword);
    }

    @Override
    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return encryptor.decrypt(encodedPassword).equals(rawPassword);
    }
}
```