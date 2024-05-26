```java
import it.geosolutions.geostore.core.security.password.GeoStorePasswordEncoder;

// existing code

public class GeoStorePBEPasswordEncoder {

    // existing code

    @Autowired
    public void setPasswordEncoder(GeoStorePasswordEncoder passwordEncoder) {
        this.passwordEncoder = passwordEncoder;
    }

    // existing code

}
```