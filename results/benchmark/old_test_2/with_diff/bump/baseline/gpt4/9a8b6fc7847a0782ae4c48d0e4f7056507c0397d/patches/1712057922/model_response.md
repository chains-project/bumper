```java
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private PBEStringEncryptor pbeStringEncryptor;

    public void setPbeStringEncryptor(PBEStringEncryptor pbeStringEncryptor) {
        this.pbeStringEncryptor = pbeStringEncryptor;
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return pbeStringEncryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return pbeStringEncryptor.decrypt(encodedPassword).equals(rawPassword.toString());
    }
}
```