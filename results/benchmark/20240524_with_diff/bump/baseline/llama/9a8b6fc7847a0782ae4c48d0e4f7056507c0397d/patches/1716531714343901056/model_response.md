```java
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder {
    private PasswordEncryptor passwordEncryptor;
    private TextEncryptor textEncryptor;

    public GeoStoreDigestPasswordEncoder(PasswordEncryptor passwordEncryptor, TextEncryptor textEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
        this.textEncryptor = textEncryptor;
    }

    public String encodePassword(String rawPass, Object salt) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(encPass, rawPass);
    }
}
```