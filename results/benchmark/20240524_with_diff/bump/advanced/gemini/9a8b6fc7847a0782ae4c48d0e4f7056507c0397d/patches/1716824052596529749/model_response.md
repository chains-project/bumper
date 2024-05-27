```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private StandardPBEStringEncryptor pbeStringEncryptor;
    private StrongPasswordEncryptor strongPasswordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setPassword(System.getenv("GEOSTORE_PASSWORD"));
        strongPasswordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String password) {
        return strongPasswordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return strongPasswordEncryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```