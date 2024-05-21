```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.password.PasswordEncodingFactoryBean;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
public class PasswordEncoderConfig {

    @Bean
    public PasswordEncodingFactoryBean passwordEncoder() {
        PasswordEncodingFactoryBean bean = new PasswordEncodingFactoryBean();
        bean.setPasswordEncryptor(new ConfigurablePasswordEncryptor());
        return bean;
    }

    @Bean
    public StandardPBEStringEncryptor standardPBEStringEncryptor() {
        return new StandardPBEStringEncryptor();
    }
}
```