```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;

public class GeoStorePBEPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword("your-password");
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations(1000);
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setConfig(config);
    }

    public String encodePassword(String password, Object salt) {
        return encryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return encryptor.checkPassword(rawPass, encPass);
    }

}
```