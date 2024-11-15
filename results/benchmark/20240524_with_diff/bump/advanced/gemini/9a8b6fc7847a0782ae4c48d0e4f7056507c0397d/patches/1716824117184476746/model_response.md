```java
import org.jasypt.encryption.pbe.StandardPBEByteEncryptor;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.PBEConfig;
import org.jasypt.exceptions.EncryptionInitializationException;
import org.jasypt.util.text.BasicTextEncryptor;
import org.springframework.beans.factory.InitializingBean;
import org.springframework.security.authentication.encoding.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder, InitializingBean {

    private StandardPBEByteEncryptor byteEncryptor;
    private StandardPBEStringEncryptor stringEncryptor;
    private String algorithm;
    private String key;
    private String salt;
    private int iterations;

    public GeoStoreDigestPasswordEncoder() {
        // Default constructor
    }

    public GeoStoreDigestPasswordEncoder(String algorithm, String key, String salt, int iterations) {
        this.algorithm = algorithm;
        this.key = key;
        this.salt = salt;
        this.iterations = iterations;
    }

    @Override
    public void afterPropertiesSet() throws Exception {
        if (algorithm == null || key == null || salt == null || iterations == 0) {
            throw new EncryptionInitializationException("All properties must be set: algorithm, key, salt, iterations");
        }

        byteEncryptor = new StandardPBEByteEncryptor();
        byteEncryptor.setAlgorithm(algorithm);
        byteEncryptor.setPassword(key);
        byteEncryptor.setSalt(salt);
        byteEncryptor.setKeyObtentionIterations(iterations);

        stringEncryptor = new StandardPBEStringEncryptor();
        stringEncryptor.setAlgorithm(algorithm);
        stringEncryptor.setPassword(key);
        stringEncryptor.setSalt(salt);
        stringEncryptor.setKeyObtentionIterations(iterations);
    }

    @Override
    public String encodePassword(String rawPassword, Object salt) {
        return stringEncryptor.encrypt(rawPassword);
    }

    @Override
    public boolean isPasswordValid(String encPassword, String rawPassword, Object salt) {
        return stringEncryptor.checkPassword(rawPassword, encPassword);
    }

    public void setAlgorithm(String algorithm) {
        this.algorithm = algorithm;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public void setSalt(String salt) {
        this.salt = salt;
    }

    public void setIterations(int iterations) {
        this.iterations = iterations;
    }
}
```