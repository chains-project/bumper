```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentStringPBEConfig;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        EnvironmentStringPBEConfig config = new EnvironmentStringPBEConfig();
        encryptor.setConfig(config);
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return rawPassword.toString().equals(encryptor.decrypt(encodedPassword));
    }
}
```