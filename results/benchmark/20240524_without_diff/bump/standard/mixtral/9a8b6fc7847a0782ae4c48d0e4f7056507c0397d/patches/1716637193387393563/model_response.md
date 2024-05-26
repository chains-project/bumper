Here's a proposed patch for the given client code:
```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    // existing code

    private BasicTextEncryptor textEncryptor = new BasicTextEncryptor();

    // existing code

    @Override
    public String encode(CharSequence rawPassword) {
        // existing code

        textEncryptor.setPassword(salt);

        // existing code
    }

    // existing code
}
```
In this patch, we replace the `PBEPasswordEncoder` class with the `BasicTextEncryptor` class from the `org.jasypt.util.text` package, which provides similar functionality. We also create a new instance of `BasicTextEncryptor` and set the salt using the `setPassword` method.