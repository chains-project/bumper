```java
import org.jasypt.password.PBEPasswordEncoder;

// Change the import from org.jasypt.spring.security.PBEPasswordEncoder;
// to org.jasypt.password.PBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder {
    // ...
    // Existing class implementation
    // ...

    // Update the following line
    // private final PBEPasswordEncoder passwordEncoder = new PBEPasswordEncoder();
    // to
    private final PBEPasswordEncoder passwordEncoder = new PBEPasswordEncoder(new StandardPBEStringEncryptor());

    // ...
    // Existing class implementation
    // ...
}
```

This patch updates the import statement and initializes the `PBEPasswordEncoder` with a `StandardPBEStringEncryptor`. This should resolve the error. However, please note that you might need to configure the `StandardPBEStringEncrypts` with the appropriate algorithm, provider, and other parameters based on your requirements.