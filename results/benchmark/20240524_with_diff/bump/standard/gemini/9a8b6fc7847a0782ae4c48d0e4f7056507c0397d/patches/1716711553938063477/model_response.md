```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private ConfigurablePasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        passwordEncryptor = new ConfigurablePasswordEncryptor();
        passwordEncryptor.setAlgorithm("SHA-1");
        passwordEncryptor.setPlainDigest(true);
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }

    public void setStringDigester(StandardPBEStringEncryptor stringDigester) {
        // Do nothing, as we don't use a string digester.
    }
}
```