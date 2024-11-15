```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentStringPBEConfig;

import java.security.SecureRandom;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private final StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder(String password) {
        EnvironmentStringPBEConfig config = new EnvironmentStringPBEConfig();
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setPoolSize(1);
        config.setProviderName("SunJCE");
        config.setSaltGenerator(new RandomSaltGenerator());
        config.setStringOutputType("base64");
        config.setPassword(password);

        encryptor = new StandardPBEStringEncryptor();
        encryptor.setConfig(config);
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encrypt(rawPassword);
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }

    private static class RandomSaltGenerator implements EnvironmentStringPBEConfig.SaltGenerator {

        @Override
        public byte[] generateSalt(EnvironmentStringPBEConfig config, String password, int saltSizeBytes) {
            byte[] salt = new byte[saltSizeBytes];
            new SecureRandom().nextBytes(salt);
            return salt;
        }

    }

}
```