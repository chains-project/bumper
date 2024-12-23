```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
public class PasswordEncoderConfig {

    @Value("${password.encryptor.password}")
    private String password;

    @Autowired
    private StandardPBEStringEncryptor encryptor;

    @Bean
    public PasswordEncoder passwordEncoder() {
        ConfigurablePasswordEncryptor passwordEncoder = new ConfigurablePasswordEncryptor();
        passwordEncoder.setEncryptor(encryptor);
        passwordEncoder.setPassword(password);
        return passwordEncoder;
    }
}
```