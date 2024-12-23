```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentPBEConfig;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        EnvironmentPBEConfig config = new EnvironmentPBEConfig();
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setPassword(System.getenv("GEOSTORE_PASSWORD"));
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setConfig(config);
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