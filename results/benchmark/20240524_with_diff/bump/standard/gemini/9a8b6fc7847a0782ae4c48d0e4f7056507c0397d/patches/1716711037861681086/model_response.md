```java
import it.geosolutions.geostore.core.security.password.GeoStorePBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
    }

    public String encodePassword(String password, Object salt) {
        return new GeoStorePBEPasswordEncoder().encodePassword(password, salt);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return new GeoStorePBEPasswordEncoder().isPasswordValid(encPass, rawPass, salt);
    }
}
```