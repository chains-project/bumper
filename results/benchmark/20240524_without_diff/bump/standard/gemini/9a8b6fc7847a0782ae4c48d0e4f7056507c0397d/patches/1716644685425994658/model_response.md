```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        this.passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encode(String password) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```