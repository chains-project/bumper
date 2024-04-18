```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStorePBEPasswordEncoder extends PasswordEncryptor {

    private PBEStringEncryptor pbeStringEncryptor;
    private TextEncryptor textEncryptor;

    public GeoStorePBEPasswordEncoder() {
        this.pbeStringEncryptor = new PBEStringEncryptor();
        this.textEncryptor = new TextEncryptor();
    }

    @Override
    public String encryptPassword(String password, Object salt) {
        return pbeStringEncryptor.encrypt(password);
    }

    @Override
    public boolean checkPassword(String password, String encryptedPassword) {
        return pbeStringEncryptor.checkPassword(password, encryptedPassword);
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }
}
```