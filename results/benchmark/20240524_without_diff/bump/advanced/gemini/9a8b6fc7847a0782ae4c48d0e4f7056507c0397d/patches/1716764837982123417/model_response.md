```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimpleStringPBEConfig;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        SimpleStringPBEConfig config = new SimpleStringPBEConfig();
        config.setPassword("geostore");
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setConfig(config);
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```