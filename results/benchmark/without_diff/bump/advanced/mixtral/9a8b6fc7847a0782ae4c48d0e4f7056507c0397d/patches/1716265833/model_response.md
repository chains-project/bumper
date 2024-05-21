Here's a proposed patch for the failing client code:
```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    // existing code

    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    // existing code

    @Override
    public String encode(CharSequence rawPassword) {
        // existing code
        encryptor.setPassword(salt);
        // existing code
    }

    // existing code
}
```
In this patch, we replace the `PBEPasswordEncoder` class from `org.jasypt.spring.security` with the `BasicTextEncryptor` class from `org.jasypt.util.text`. This allows us to continue encrypting passwords without relying on the external dependency that has been updated and is causing issues. We also create a new `encryptor` variable to hold an instance of `BasicTextEncryptor`, which we use in the `encode` method.