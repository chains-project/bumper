```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentStringPBEConfig;
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();

    public GeoStorePBEPasswordEncoder() {
        EnvironmentStringPBEConfig config = new EnvironmentStringPBEConfig();
        config.setPassword("password");
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setProviderName("SunJCE");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setStringOutputType("base64");
        encryptor.setConfig(config);
    }

    public String encodePassword(String password, Object salt) {
        return encryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword, Object salt) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```