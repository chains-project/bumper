```java
import org.jasypt.util.password.StrongPasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        this.passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encPassword);
    }
}
```