```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePasswordEncoder() {
        this.passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```