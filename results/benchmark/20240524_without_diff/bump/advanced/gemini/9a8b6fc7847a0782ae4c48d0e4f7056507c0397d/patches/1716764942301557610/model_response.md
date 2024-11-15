```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private static final String ALGORITHM = "PBEWithMD5AndDES";
    private static final String DEFAULT_SALT = "GeoStoreSalt";

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(DEFAULT_SALT);
        encryptor.setAlgorithm(ALGORITHM);
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.decrypt(encodedPassword).equals(rawPassword.toString());
    }
}
```