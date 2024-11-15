```java
import org.jasypt.encryption.StringEncryptor;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.crypto.password.PasswordEncoder;

@Configuration
public class SecurityConfig {

    @Autowired
    private StringEncryptor stringEncryptor;

    @Bean
    public PasswordEncoder passwordEncoder() {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        passwordEncryptor.setPasswordEncoder(new PBEPasswordEncoder(stringEncryptor));
        return passwordEncryptor;
    }

    private static class PBEPasswordEncoder implements org.jasypt.util.password.PasswordEncryptor {

        private final StringEncryptor stringEncryptor;

        public PBEPasswordEncoder(StringEncryptor stringEncryptor) {
            this.stringEncryptor = stringEncryptor;
        }

        @Override
        public String encryptPassword(String password) {
            return stringEncryptor.encrypt(password);
        }

        @Override
        public boolean checkPassword(String plainPassword, String encodedPassword) {
            return stringEncryptor.decrypt(encodedPassword).equals(plainPassword);
        }
    }
}
```