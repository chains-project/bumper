```java
import org.jasypt.encryption.pbe.StandardPBEPasswordEncoder;

public class GeoStoreDigestPasswordEncoder {
    private StandardPBEPasswordEncoder passwordEncoder;

    public GeoStoreDigestPasswordEncoder() {
        passwordEncoder = new StandardPBEPasswordEncoder();
    }

    public String encodePassword(String rawPass, Object salt) {
        return passwordEncoder.encodePassword(rawPass, salt);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncoder.isPasswordValid(encPass, rawPass, salt);
    }
}
```