```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder extends StrongPasswordEncryptor {

    public GeoStorePBEPasswordEncoder(String password, String salt) {
        super(password, salt);
    }

    public GeoStorePBEPasswordEncoder(String password) {
        super(password);
    }

    public GeoStorePBEPasswordEncoder() {
        super();
    }

    @Override
    public String encodePassword(String rawPassword, Object salt) {
        return super.encodePassword(rawPassword, salt);
    }

    @Override
    public boolean checkPassword(String rawPassword, String encodedPassword) {
        return super.checkPassword(rawPassword, encodedPassword);
    }
}
```