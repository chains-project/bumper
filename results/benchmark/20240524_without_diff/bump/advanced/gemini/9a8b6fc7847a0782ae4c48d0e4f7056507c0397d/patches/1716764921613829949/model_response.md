```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder(String password) {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(password);
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```