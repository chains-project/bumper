```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder extends PasswordEncoder {

    private StandardPBEStringEncryptor pbeStringEncryptor;
    private StrongTextEncryptor textEncryptor;

    public GeoStorePBEPasswordEncoder() {
        pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setPassword("password");
        textEncryptor = new StrongTextEncryptor();
        textEncryptor.setPassword("password");
    }

    @Override
    public String encodePassword(String rawPassword, Object salt) {
        return pbeStringEncryptor.encrypt(rawPassword);
    }

    @Override
    public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
        return pbeStringEncryptor.checkPassword(rawPassword, encPassword);
    }

    public void setPbeStringEncryptor(StandardPBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    public void setTextEncryptor(StrongTextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }
}
```