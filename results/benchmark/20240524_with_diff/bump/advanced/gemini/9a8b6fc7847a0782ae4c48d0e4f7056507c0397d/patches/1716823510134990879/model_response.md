```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor pbeStringEncryptor;
    private BasicTextEncryptor textEncryptor;

    public GeoStorePBEPasswordEncoder() {
        pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setPassword("your_password");
        textEncryptor = new BasicTextEncryptor();
        textEncryptor.setPassword("your_password");
    }

    public String encodePassword(String password, Object salt) {
        return pbeStringEncryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return pbeStringEncryptor.checkPassword(rawPassword, encodedPassword);
    }

    public void setPbeStringEncryptor(StandardPBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(BasicTextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }
}
```