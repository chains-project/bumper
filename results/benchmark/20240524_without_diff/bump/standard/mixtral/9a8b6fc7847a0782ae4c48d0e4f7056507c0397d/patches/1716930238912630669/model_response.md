Here's a proposed patch for the failing client code:
```java
import org.jasypt.password.PBEPasswordEncoder;

// Change the import statement to use the top-level package of Jasypt
// instead of the Spring-specific package

// ... (existing code) ...

@Component
public class GeoStorePBEPasswordEncoder extends PBEPasswordEncoder {
  // ... (existing code) ...
}
```
Note that the `PBEPasswordEncoder` class is still being used, but the import statement has been changed to use the top-level package of Jasypt instead of the Spring-specific package. This should fix the error message indicating that the `org.jasypt.spring.security` package does not exist.