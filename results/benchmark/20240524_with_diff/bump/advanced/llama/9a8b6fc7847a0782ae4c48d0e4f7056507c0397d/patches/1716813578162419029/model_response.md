```java
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```