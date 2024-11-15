```java
import org.jasypt.springsecurity.configuration.SecurityConfig;
import org.jasypt.springsecurity.encryptable.PasswordEncryptor;

public class GeoStorePBEPasswordEncoder {
    private final PasswordEncryptor passwordEncryptor;

    public GeoStorePBEPasswordEncoder(String password) {
        this.passwordEncryptor = new org.jasypt.springsecurity.encryptable.PasswordEncryptor() {
            @Override
            public String encryptPassword(String password) {
                return password;
            }

            @Override
            public boolean verifyPassword(String providedPassword, String encryptedPassword) {
                return providedPassword.equals(encryptedPassword);
            }
        };
    }

    public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword.toString());
    }

    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.verifyPassword(rawPassword.toString(), encodedPassword);
    }
}
```