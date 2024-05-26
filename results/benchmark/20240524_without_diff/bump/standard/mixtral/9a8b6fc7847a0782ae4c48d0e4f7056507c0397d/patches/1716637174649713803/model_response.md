```java
import it.geosolutions.geostore.core.security.password.GeoStorePasswordEncoder;

// existing code

public class GeoStorePBEPasswordEncoder implements PasswordEncoder {

    // existing code

    private final GeoStorePasswordEncoder passwordEncoder;

    // existing code

    public GeoSpringProjectTest() {
        // existing code
        this.passwordEncoder = new GeoStorePasswordEncoder();
        // existing code
    }

    // existing code

}

```

This code snippet removes the dependency on `org.jasypt.spring.security` by using a custom `GeoStorePasswordEncoder` instead of `PBEPasswordEncoder`. The `GeoStorePasswordEncoder` is assumed to have the same functionality as `PBEPasswordEncoder`.