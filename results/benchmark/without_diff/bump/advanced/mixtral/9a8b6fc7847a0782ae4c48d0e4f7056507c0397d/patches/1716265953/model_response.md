Here is the proposed patch:

```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    // existing code...

    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    // existing code...

    @Override
    public String encode(CharSequence rawPassword) {
        // existing code...
        encryptor.setPassword(salt);
        // existing code...
    }

    // existing code...
}
```

In this patch, we replace the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package with the `BasicTextEncryptor` class from the `org.jasypt.util.text` package. This allows us to continue encrypting passwords using the same logic as before, but without relying on the now-unavailable `PBEPasswordEncoder` class. We also create a new instance of `BasicTextEncryptor` and set its password using the `setPassword` method.