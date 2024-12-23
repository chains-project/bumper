```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.PBEConfig;
import org.jasypt.exceptions.EncryptionOperationNotPossibleException;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder(String password, String salt) {
        this(password, salt, null);
    }

    public GeoStorePBEPasswordEncoder(String password, String salt, String algorithm) {
        encryptor = new StandardPBEStringEncryptor();
        PBEConfig config = new PBEConfig();
        config.setPassword(password);
        config.setSalt(salt);
        if (algorithm != null) {
            config.setAlgorithm(algorithm);
        }
        encryptor.setConfig(config);
    }

    @Override
    public String encode(CharSequence rawPassword) {
        try {
            return encryptor.encrypt(rawPassword.toString());
        } catch (EncryptionOperationNotPossibleException e) {
            throw new RuntimeException("Failed to encode password", e);
        }
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        try {
            return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
        } catch (EncryptionOperationNotPossibleException e) {
            throw new RuntimeException("Failed to match password", e);
        }
    }
}
```