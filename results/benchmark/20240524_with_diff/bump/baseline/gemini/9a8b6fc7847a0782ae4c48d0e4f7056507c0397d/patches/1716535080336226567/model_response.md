```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder(PBEStringEncryptor pbeStringEncryptor) {
        this.passwordEncryptor = new StrongPasswordEncryptor();
        this.passwordEncryptor.setPassword(pbeStringEncryptor.getPassword());
    }

    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encPassword);
    }
}
```