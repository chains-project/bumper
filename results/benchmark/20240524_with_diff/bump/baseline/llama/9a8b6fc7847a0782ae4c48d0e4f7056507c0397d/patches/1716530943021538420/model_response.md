```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        this.passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String rawPass, Object salt) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```