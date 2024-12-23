```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentStringPBEConfig;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {
    private TextEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        EnvironmentStringPBEConfig config = new EnvironmentStringPBEConfig();
        config.setPasswordEnvName("ENC_PASSWORD");
        encryptor.setConfig(config);
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return encryptor.encrypt(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        String encRawPass = encryptor.encrypt(rawPass);
        return encRawPass.equals(encPass);
    }
}
```