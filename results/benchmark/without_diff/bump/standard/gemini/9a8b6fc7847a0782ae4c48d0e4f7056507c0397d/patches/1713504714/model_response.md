```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder(String password) {
        this.encryptor = new StandardPBEStringEncryptor();
        this.encryptor.setPassword(password);
    }

    public String encode(String plainText) {
        return this.encryptor.encrypt(plainText);
    }

    public boolean matches(String plainText, String encodedText) {
        return this.encryptor.checkPassword(plainText, encodedText);
    }
}
```