```java
import org.jasypt.encryption.pbe.StandardPBEByteEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentPBEConfig;
import org.jasypt.util.text.StrongTextEncryptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.context.annotation.PropertySource;
import org.springframework.core.env.Environment;

@Configuration
@PropertySource("classpath:application.properties")
public class PBEPasswordEncoderConfig {

    @Autowired
    private Environment env;

    @Value("${jasypt.encryptor.password}")
    private String password;

    @Bean
    public StandardPBEByteEncryptor standardPBEByteEncryptor() {
        StandardPBEByteEncryptor encryptor = new StandardPBEByteEncryptor();
        EnvironmentPBEConfig config = new EnvironmentPBEConfig();
        config.setAlgorithm(env.getProperty("jasypt.encryptor.algorithm"));
        config.setKeyObtentionIterations(env.getProperty("jasypt.encryptor.keyObtentionIterations", Integer.class));
        config.setPoolSize(env.getProperty("jasypt.encryptor.poolSize", Integer.class));
        config.setProviderName(env.getProperty("jasypt.encryptor.providerName"));
        config.setSaltGeneratorClassName(env.getProperty("jasypt.encryptor.saltGeneratorClassName"));
        config.setStringOutputType(env.getProperty("jasypt.encryptor.stringOutputType"));
        encryptor.setConfig(config);
        encryptor.setPassword(password);
        return encryptor;
    }

    @Bean
    public StrongTextEncryptor strongTextEncryptor() {
        StrongTextEncryptor encryptor = new StrongTextEncryptor();
        encryptor.setAlgorithm(env.getProperty("jasypt.encryptor.algorithm"));
        encryptor.setKeyObtentionIterations(env.getProperty("jasypt.encryptor.keyObtentionIterations", Integer.class));
        encryptor.setPoolSize(env.getProperty("jasypt.encryptor.poolSize", Integer.class));
        encryptor.setProviderName(env.getProperty("jasypt.encryptor.providerName"));
        encryptor.setSaltGeneratorClassName(env.getProperty("jasypt.encryptor.saltGeneratorClassName"));
        encryptor.setStringOutputType(env.getProperty("jasypt.encryptor.stringOutputType"));
        encryptor.setPassword(password);
        return encryptor;
    }
}
```