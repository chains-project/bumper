```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private PBEStringEncryptor pbeStringEncryptor;
    private TextEncryptor textEncryptor;

    public GeoStorePBEPasswordEncoder() {
        this.pbeStringEncryptor = new PBEStringEncryptor();
        this.textEncryptor = new TextEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        return this.pbeStringEncryptor.encrypt(password);
    }

    public boolean isPasswordValid(String password, String encodedPassword, Object salt) {
        return this.pbeStringEncryptor.decrypt(encodedPassword).equals(password);
    }

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }
}
```