```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;
    private final StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        this.encryptor = new StandardPBEStringEncryptor();
        this.encryptor.setPassword("your_secret_password");
        this.passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```