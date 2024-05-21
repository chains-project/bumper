```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    private final StandardPBEStringEncryptor pbeStringEncryptor;
    private final StrongPasswordEncryptor strongPasswordEncryptor;

    public GeoStorePBEPasswordEncoder() {
        pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setPassword("geosolutions");
        pbeStringEncryptor.setAlgorithm("PBEWithMD5AndDES");

        strongPasswordEncryptor = new StrongPasswordEncryptor();
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return strongPasswordEncryptor.encode(rawPassword);
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return strongPasswordEncryptor.matches(rawPassword, encodedPassword);
    }

    public String encodePassword(String password, Object salt) {
        return pbeStringEncryptor.encrypt(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return pbeStringEncryptor.checkPassword(rawPass, encPass);
    }
}
```