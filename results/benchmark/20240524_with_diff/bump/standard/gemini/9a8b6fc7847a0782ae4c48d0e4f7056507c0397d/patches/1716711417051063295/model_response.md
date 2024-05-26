```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private PasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder(PasswordEncryptor passwordEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
    }

    public String encodePassword(String password, Object salt) {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(passwordEncryptor.encryptPassword(password));
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(passwordEncryptor.encryptPassword(rawPass));
        return encryptor.checkPassword(encPass, rawPass);
    }
}
```