```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentPBEConfig;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        EnvironmentPBEConfig config = new EnvironmentPBEConfig();
        config.setAlgorithm("PBEWithMD5AndTripleDES");
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