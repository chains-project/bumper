```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {

    public GeoStorePBEPasswordEncoder(String password) {
        setPassword(password);
    }

    public String encode(String password) {
        return encrypt(password);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return checkPassword(rawPassword, encodedPassword);
    }
}
```