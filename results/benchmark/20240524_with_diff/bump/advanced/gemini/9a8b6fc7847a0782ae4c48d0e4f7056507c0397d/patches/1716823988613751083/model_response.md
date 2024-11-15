```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {

    private static final String ALGORITHM = "PBEWithMD5AndDES";

    private final ConfigurablePasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        passwordEncryptor = new ConfigurablePasswordEncryptor();
        passwordEncryptor.setAlgorithm(ALGORITHM);
        passwordEncryptor.setPlainDigest(true);
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```