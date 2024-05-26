```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentStringPBEConfig;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {
    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        EnvironmentStringPBEConfig config = new EnvironmentStringPBEConfig();
        encryptor.setConfig(config);
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return encryptor.encrypt(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        String encryptedPass = encryptor.encrypt(rawPass);
        return encryptedPass.equals(encPass);
    }
}
```