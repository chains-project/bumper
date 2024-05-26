```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("password");
        encryptor.setAlgorithm("PBEWithMD5AndDES");
    }

    public String encodePassword(String password) {
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return encryptor.decrypt(encodedPassword).equals(rawPassword);
    }
}
```