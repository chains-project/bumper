```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStoreDigestPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("password");
    }

    public String encodePassword(String password, Object salt) {
        ConfigurablePasswordEncryptor passwordEncryptor = new ConfigurablePasswordEncryptor();
        passwordEncryptor.setAlgorithm("SHA-1");
        passwordEncryptor.setStringEncryptor(encryptor);
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        ConfigurablePasswordEncryptor passwordEncryptor = new ConfigurablePasswordEncryptor();
        passwordEncryptor.setAlgorithm("SHA-1");
        passwordEncryptor.setStringEncryptor(encryptor);
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```