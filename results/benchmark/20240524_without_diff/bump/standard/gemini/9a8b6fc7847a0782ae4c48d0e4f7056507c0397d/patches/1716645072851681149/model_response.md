```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;

public class GeoStoreDigestPasswordEncoder {

    private StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();

    public GeoStoreDigestPasswordEncoder() {
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword("password");
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        encryptor.setConfig(config);
    }

    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword);
    }

    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```