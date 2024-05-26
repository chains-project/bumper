Here'Fully qualified code to fix the error:

~~~java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder {

    private final PasswordEncoder passwordEncoder;

    public GeoStoreDigestPasswordEncoder() {
        this.passwordEncoder = new BasicPasswordEncryptor();
    }

    public String encodePassword(String rawPassword) {
        return passwordEncoder.encode(rawPassword);
    }

    public boolean isPasswordValid(String encodata, String rawPassword) {
        return passwordEncoder.matches(rawPassword, encodata);
    }
}
~~~