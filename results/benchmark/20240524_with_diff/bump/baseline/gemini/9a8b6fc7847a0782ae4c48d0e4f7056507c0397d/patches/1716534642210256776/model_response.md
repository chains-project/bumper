```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor pbeStringEncryptor;

    public GeoStorePBEPasswordEncoder() {
        pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setPassword(new StrongPasswordEncryptor().createPassword());
    }

    public String encodePassword(String password, Object salt) {
        pbeStringEncryptor.setSalt(salt);
        return pbeStringEncryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        pbeStringEncryptor.setSalt(salt);
        return pbeStringEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```