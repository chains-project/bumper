```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("password"); // Replace with your actual password
        encryptor.setAlgorithm("PBEWithMD5AndDES"); // Choose a suitable encryption algorithm
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