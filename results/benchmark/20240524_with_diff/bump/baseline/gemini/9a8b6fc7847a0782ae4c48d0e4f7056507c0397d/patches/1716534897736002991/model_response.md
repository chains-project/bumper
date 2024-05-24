```java
import org.jasypt.util.password.PasswordEncryptor;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class GeoStoreDigestPasswordEncoder {

    @Autowired
    private PasswordEncryptor passwordEncryptor;

    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```