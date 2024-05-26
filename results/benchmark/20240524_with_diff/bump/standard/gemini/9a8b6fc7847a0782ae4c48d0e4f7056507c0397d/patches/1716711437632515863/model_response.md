```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("geostore");
    }

    @Override
    public String encodePassword(String rawPassword, Object salt) {
        return encryptor.encrypt(rawPassword);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return encryptor.decrypt(encPass).equals(rawPass);
    }
}
```