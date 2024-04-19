```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("geosolutions");
    }

    public String encodePassword(String password, Object salt) {
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```