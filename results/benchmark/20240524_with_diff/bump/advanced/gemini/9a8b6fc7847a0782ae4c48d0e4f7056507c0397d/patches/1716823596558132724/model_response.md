```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder as SpringPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends SpringPasswordEncoder {

    @Autowired
    private PasswordEncryptor passwordEncryptor;

    @Override
    public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }

    public void setPasswordEncoder(PasswordEncryptor passwordEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
    }
}
```