```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private PBEStringEncryptor pbeStringEncryptor;
    private TextEncryptor textEncryptor;
    private PasswordEncryptor passwordEncryptor;

    // Constructor removed, no longer needed

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }

    public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
    }
}
```