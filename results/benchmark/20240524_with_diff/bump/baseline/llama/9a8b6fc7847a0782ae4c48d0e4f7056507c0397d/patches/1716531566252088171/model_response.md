```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    public String encodePassword(String rawPass, Object salt) {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```