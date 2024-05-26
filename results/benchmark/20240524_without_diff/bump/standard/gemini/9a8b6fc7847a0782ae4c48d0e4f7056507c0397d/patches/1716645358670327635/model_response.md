```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentPBEConfig;
import org.jasypt.spring.security.PBEPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

/**
 * GeoStore specific password encoder.
 */
public class GeoStorePBEPasswordEncoder extends PBEPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder(String password, String salt) {
        this(password, salt, null);
    }

    public GeoStorePBEPasswordEncoder(String password, String salt, String algorithm) {
        super(password, salt, algorithm);
        this.encryptor = new StandardPBEStringEncryptor();
        EnvironmentPBEConfig config = new EnvironmentPBEConfig();
        config.setAlgorithm(algorithm);
        config.setPassword(password);
        config.setSalt(salt);
        encryptor.setConfig(config);
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