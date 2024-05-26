```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder(String password) {
        this.encryptor = new StandardPBEStringEncryptor();
        this.encryptor.setPassword(password);
    }

    public String encode(String rawPassword) {
        return this.encryptor.encrypt(rawPassword);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return this.encryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```