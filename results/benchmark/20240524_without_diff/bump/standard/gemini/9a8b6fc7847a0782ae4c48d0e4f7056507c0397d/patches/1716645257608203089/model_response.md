```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder(String password) {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(password);
    }

    public String encode(String password) {
        return encryptor.encrypt(password);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```