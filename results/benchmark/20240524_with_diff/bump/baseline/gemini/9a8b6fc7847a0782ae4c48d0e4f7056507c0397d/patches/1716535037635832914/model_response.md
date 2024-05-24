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

    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
        return passwordEncryptor.checkPassword(rawPassword, encPassword);
    }

    public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }
}
```