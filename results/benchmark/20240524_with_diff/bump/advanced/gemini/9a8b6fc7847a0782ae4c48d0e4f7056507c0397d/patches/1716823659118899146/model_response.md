```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private final PasswordEncoder passwordEncoder;

    public GeoStorePBEPasswordEncoder() {
        StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword(System.getenv("GEOSTORE_SECRET"));
        encryptor.setAlgorithm("PBEWithMD5AndDES");

        ConfigurablePasswordEncryptor passwordEncryptor = new ConfigurablePasswordEncryptor();
        passwordEncryptor.setEncryptor(encryptor);

        this.passwordEncoder = new PasswordEncoder();
        this.passwordEncoder.setPasswordEncryptor(passwordEncryptor);
    }

    public String encodePassword(String password) {
        return passwordEncoder.encodePassword(password, null);
    }

    public boolean isPasswordValid(String encodedPassword, String rawPassword) {
        return passwordEncoder.isPasswordValid(encodedPassword, rawPassword, null);
    }
}
```