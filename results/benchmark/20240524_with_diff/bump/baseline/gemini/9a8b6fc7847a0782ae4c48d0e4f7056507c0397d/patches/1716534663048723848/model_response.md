```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor pbeStringEncryptor;

    public GeoStorePBEPasswordEncoder() {
        pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setPassword("your_password");
    }

    public String encodePassword(String password) {
        return pbeStringEncryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return pbeStringEncryptor.checkPassword(rawPassword, encodedPassword);
    }

    public void setPbeStringEncryptor(StandardPBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }
}
```