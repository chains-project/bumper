```java
import org.springframework.security.crypto.password.PBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends PBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
    }

    public GeoStorePBEPasswordEncoder(String salt) {
        super(salt);
    }

    public GeoStorePBEPasswordEncoder(String salt, int iterations) {
        super(salt, iterations);
    }

    public GeoStorePBEPasswordEncoder(String salt, int iterations, int hashWidth) {
        super(salt, iterations, hashWidth);
    }

    public GeoStorePBEPasswordEncoder(String salt, int iterations, int hashWidth, String algorithm) {
        super(salt, iterations, hashWidth, algorithm);
    }

    public GeoStorePBEPasswordEncoder(String salt, int iterations, int hashWidth, String algorithm, boolean encodeHashAsBase64) {
        super(salt, iterations, hashWidth, algorithm, encodeHashAsBase64);
    }
}
```