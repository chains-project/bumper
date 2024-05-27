```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;

public class GeoStorePBEPasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder(String password) {
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword(password);
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setIvGeneratorClassName("org.jasypt.iv.RandomIvGenerator");
        config.setStringOutputType("base64");
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setConfig(config);
    }

    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword);
    }

    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```