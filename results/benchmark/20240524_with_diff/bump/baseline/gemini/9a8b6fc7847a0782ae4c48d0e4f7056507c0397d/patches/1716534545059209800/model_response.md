```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("your_password");
    }

    public String encodePassword(String password) {
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }

}
```