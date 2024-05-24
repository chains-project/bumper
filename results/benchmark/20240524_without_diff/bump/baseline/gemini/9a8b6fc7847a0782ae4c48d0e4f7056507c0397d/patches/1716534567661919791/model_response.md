```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        encryptor.setPassword(salt.toString());
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        encryptor.setPassword(salt.toString());
        return encryptor.decrypt(encodedPassword).equals(rawPassword);
    }

    public void setPbeStringEncryptor(StandardPBEStringEncryptor encryptor) {
        this.encryptor = encryptor;
    }
}
```