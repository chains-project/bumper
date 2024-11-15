```java
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.encryption.pbe.PBEStringEncryptor;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private PasswordEncryptor passwordEncryptor;
    private PBEStringEncryptor pbeStringEncryptor;

    public GeoStoreDigestPasswordEncoder(PasswordEncryptor passwordEncryptor, PBEStringEncryptor pbeStringEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }

    public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }
}
```