```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        passwordEncryptor = new StrongPasswordEncryptor();
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```