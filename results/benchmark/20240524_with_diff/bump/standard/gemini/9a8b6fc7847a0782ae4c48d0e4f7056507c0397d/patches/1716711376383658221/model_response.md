```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private ConfigurablePasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        passwordEncryptor = new ConfigurablePasswordEncryptor();
        passwordEncryptor.setAlgorithm("SHA-1");
        passwordEncryptor.setPlainDigest(true);
    }

    @Override
    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncryptor.encryptPassword(rawPassword);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }

    public void setPasswordEncryptor(ConfigurablePasswordEncryptor passwordEncryptor) {
        this.passwordEncryptor = passwordEncryptor;
    }
}
```