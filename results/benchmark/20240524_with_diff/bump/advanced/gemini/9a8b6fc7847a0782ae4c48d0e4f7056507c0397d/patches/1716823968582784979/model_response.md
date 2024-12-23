```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.SimplePBEConfig;
import org.jasypt.util.text.BasicTextEncryptor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
@PropertySource("classpath:application.properties")
public class PasswordEncoderConfig {

    @Value("${jasypt.encryptor.password}")
    private String password;

    @Bean
    public PasswordEncoder passwordEncoder() {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        SimplePBEConfig config = new SimplePBEConfig();
        config.setPassword(password);
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setProviderName("SunJCE");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setStringOutputType("base64");
        encryptor.setConfig(config);
        return new GeoStoreDigestPasswordEncoder(encryptor);
    }
}
```