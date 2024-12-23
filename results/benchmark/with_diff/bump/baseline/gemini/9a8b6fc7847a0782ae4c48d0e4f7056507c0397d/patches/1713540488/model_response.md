```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private PBEStringEncryptor pbeStringEncryptor;
    private TextEncryptor textEncryptor;

    public GeoStorePBEPasswordEncoder(PBEStringEncryptor pbeStringEncryptor, TextEncryptor textEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
        this.textEncryptor = textEncryptor;
    }

    public String encodePassword(String password, Object salt) {
        return pbeStringEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
        return pbeStringEncryptor.checkPassword(rawPassword, encPassword);
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }
}
```