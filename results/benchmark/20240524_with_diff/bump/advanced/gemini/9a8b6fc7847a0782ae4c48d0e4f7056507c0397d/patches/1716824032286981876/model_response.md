```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```