```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {

    private final String password;

    public GeoStorePBEPasswordEncoder(String password) {
        this.password = password;
        this.setPassword(password);
    }

    public String encode(String input) {
        return encrypt(input, password);
    }

    public boolean matches(String input, String encoded) {
        return checkPassword(input, encoded);
    }
}
```