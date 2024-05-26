```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder(String password, String salt) {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(password);
        encryptor.setAlgorithm("PBEWithMD5AndDES");
        encryptor.setSalt(salt);

        passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String rawPassword) {
        return encryptor.encrypt(rawPassword);
    }

    public boolean isPasswordValid(String rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```