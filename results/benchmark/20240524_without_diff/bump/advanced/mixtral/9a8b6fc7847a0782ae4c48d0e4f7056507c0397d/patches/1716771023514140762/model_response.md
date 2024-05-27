Here is a proposed patch for the failing client code:

```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    // existing code...

    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    // existing code...

    @Override
    public String encode(CharSequence rawPassword) {
        // existing code...
        encryptor.setPassword(passwordSalt);
        // existing code...
    }

    // existing code...
}
```
In this patch, we replace the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package with the `BasicTextEncryptor` class from the `org.jasypt.util.text` package. We also create a new instance of `BasicTextEncryptor` and use it to replace the functionality of the `PBEPasswordEncoder` class.

Note that this patch assumes that the rest of the `GeoStorePBEPasswordEncoder` class is unchanged and that the `passwordSalt` variable is defined and accessible within the `encode` method. If this is not the case, the patch may need to be modified accordingly.