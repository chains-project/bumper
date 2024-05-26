```java
import org.jasypt.password.PBEPasswordEncoder;

// Change the type of the variable to the new imported class
public class GeoStorePBEPasswordEncoder {

    // ...

    private final PBEPasswordEncoder passwordEncoder;

    // ...
}
```

In this case, the `org.jasypt.spring.security.PBEPasswordEncoder` class is not found. I replaced it with `org.jasypt.password.PBEPasswordEncoder` which should be part of the same library.

This change will require you to update the initialization and usage of the `passwordEncoder` variable accordingly.