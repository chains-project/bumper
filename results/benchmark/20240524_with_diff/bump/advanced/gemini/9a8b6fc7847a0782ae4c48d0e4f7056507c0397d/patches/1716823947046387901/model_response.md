```java
import org.jasypt.encryption.pbe.StandardPBEByteEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentPBEConfig;
import org.jasypt.encryption.pbe.config.SimplePBEConfig;
import org.jasypt.exceptions.EncryptionOperationNotPossibleException;
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;

import javax.annotation.PostConstruct;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.Properties;

@Configuration
public class PasswordEncoderConfig {

    private static final Logger LOGGER = LoggerFactory.getLogger(PasswordEncoderConfig.class);

    @Value("${geoStore.password.salt}")
    private String salt;

    @Value("${geoStore.password.algorithm}")
    private String algorithm;

    @Value("${geoStore.password.iterations}")
    private int iterations;

    @Value("${geoStore.password.key-obfuscation-salt}")
    private String keyObfuscationSalt;

    @Value("${geoStore.password.string-obfuscator.password}")
    private String stringObfuscatorPassword;

    @Value("${geoStore.password.digest.algorithm}")
    private String digestAlgorithm;

    @Value("${geoStore.password.digest.salt-size-bytes}")
    private int digestSaltSizeBytes;

    @Value("${geoStore.password.digest.iterations}")
    private int digestIterations;

    @Autowired
    private GeoStoreProperties geoStoreProperties;

    @Bean
    public PasswordEncoder passwordEncoder() {
        return new BCryptPasswordEncoder();
    }

    @Bean
    public PasswordEncryptor passwordEncryptor() {
        BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();
        passwordEncryptor.setPassword(stringObfuscatorPassword);
        return passwordEncryptor;
    }

    @Bean
    public StandardPBEByteEncryptor standardPBEByteEncryptor() {
        StandardPBEByteEncryptor standardPBEByteEncryptor = new StandardPBEByteEncryptor();
        standardPBEByteEncryptor.setConfig(environmentPBEConfig());
        return standardPBEByteEncryptor;
    }

    @Bean
    public EnvironmentPBEConfig environmentPBEConfig() {
        EnvironmentPBEConfig environmentPBEConfig = new EnvironmentPBEConfig();
        environmentPBEConfig.setAlgorithm(algorithm);
        environmentPBEConfig.setPassword(salt);
        environmentPBEConfig.setPoolSize("1");
        environmentPBEConfig.setProviderName(null);
        environmentPBEConfig.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        environmentPBEConfig.setStringOutputType("base64");
        return environmentPBEConfig;
    }

    @PostConstruct
    public void init() throws IOException {
        Properties properties = new Properties();
        properties.load(GeoStoreDigestPasswordEncoder.class.getResourceAsStream("/geoStore-password.properties"));

        String password = properties.getProperty("geoStore.password");
        if (password == null || password.isEmpty()) {
            LOGGER.warn("No password found in geoStore-password.properties file. Using default password.");
            return;
        }

        try {
            standardPBEByteEncryptor().decrypt(password);
        } catch (EncryptionOperationNotPossibleException e) {
            LOGGER.error("Error decrypting password from geoStore-password.properties file. Using default password.", e);
        }
    }
}
```