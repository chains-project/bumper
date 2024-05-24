```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private StandardPBEStringEncryptor pbeStringEncryptor;
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setPassword("secret");
        passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```