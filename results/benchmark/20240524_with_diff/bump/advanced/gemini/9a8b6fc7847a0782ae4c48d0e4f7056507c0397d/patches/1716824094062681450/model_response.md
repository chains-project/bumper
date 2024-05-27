```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.salt.RandomSaltGenerator;
import org.jasypt.util.text.BasicTextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private static final String ALGORITHM = "PBEWithMD5AndDES";
    private static final int KEY_OBTENTION_ITERATIONS = 1000;
    private static final int POOL_SIZE = 1;

    private final PBEStringEncryptor pbeStringEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        this.pbeStringEncryptor = new StandardPBEStringEncryptor();
        pbeStringEncryptor.setAlgorithm(ALGORITHM);
        pbeStringEncryptor.setKeyObtentionIterations(KEY_OBTENTION_ITERATIONS);
        pbeStringEncryptor.setPoolSize(POOL_SIZE);
        pbeStringEncryptor.setSaltGenerator(new RandomSaltGenerator());
        pbeStringEncryptor.setPassword(System.getenv("GEOSTORE_PASSWORD"));
    }

    @Override
    public String encode(CharSequence rawPassword) {
        return pbeStringEncryptor.encrypt(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return pbeStringEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```