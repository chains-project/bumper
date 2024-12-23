```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;
    private final StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("mySecretKey");
        passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encPassword, String rawPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encPassword);
    }
}
```