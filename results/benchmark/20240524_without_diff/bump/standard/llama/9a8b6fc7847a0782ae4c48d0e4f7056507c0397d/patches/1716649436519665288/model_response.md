```java
import org.jasypt.springsecurity.config.SecurityConfig;
import org.jasypt.springsecurity.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.springsecurity.encryption.pbe.config.EnvironmentPBEConfig;

public class GeoStorePBEPasswordEncoder extends org.springframework.security.authentication.encoding.PasswordEncoder {
    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        EnvironmentPBEConfig config = new EnvironmentPBEConfig();
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setConfig(config);
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return encryptor.encrypt(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return encryptor.decrypt(encPass).equals(rawPass);
    }
}
```