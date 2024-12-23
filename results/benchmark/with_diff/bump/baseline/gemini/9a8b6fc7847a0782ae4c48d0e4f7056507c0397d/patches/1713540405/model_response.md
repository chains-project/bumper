```java
import org.jasypt.encryption.pbe.PBEEncryptor;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.PBEConfig;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final ConfigurablePasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        PBEConfig config = new PBEConfig();
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setProviderName("SunJCE");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setStringOutputType("base64");

        PBEEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setConfig(config);

        passwordEncryptor = new ConfigurablePasswordEncryptor();
        passwordEncryptor.setEncryptor(encryptor);
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```