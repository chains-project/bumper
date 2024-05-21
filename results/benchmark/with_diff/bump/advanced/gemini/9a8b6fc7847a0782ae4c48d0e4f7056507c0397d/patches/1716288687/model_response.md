```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;
    private final StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(System.getenv("GEOSTORE_PASSWORD"));
        passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String password) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```