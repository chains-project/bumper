```java
import org.jasypt.encryption.pbe.config.PBEConfig;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
public class SecurityConfig {

    @Value("${jasypt.encryptor.password}")
    private String encryptorPassword;

    @Bean
    public PasswordEncoder passwordEncoder() {
        PBEStringEncryptor encryptor = new PBEStringEncryptor();
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        PBEConfig config = new PBEConfig();
        config.setPassword(encryptorPassword);
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setKeyObtentionIterations("1000");
        config.setPoolSize("1");
        config.setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        config.setProviderName("SunJCE");
        config.setIvGeneratorClassName("org.jasypt.iv.RandomIvGenerator");
        config.setStringOutputType("base64");
        encryptor.setConfig(config);
        passwordEncryptor.setPasswordEncoder(encryptor);
        return passwordEncryptor;
    }
}
```