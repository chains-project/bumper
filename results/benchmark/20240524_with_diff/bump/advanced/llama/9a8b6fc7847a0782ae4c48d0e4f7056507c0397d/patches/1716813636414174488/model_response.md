```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
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