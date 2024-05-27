Here's a proposed patch that replaces the failing client code:
```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    // existing code
    private BasicTextEncryptor encryptor = new BasicTextEncryptor();
    // existing code

    public void setPassword(String password) {
        // existing code
        encryptor.setPassword(password);
        // existing code
    }

    public String encode(String plainText) {
        // existing code
        return encryptor.encrypt(plainText);
        // existing code
    }

    // existing code
}
```
In this patch, I replaced the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package with the `BasicTextEncryptor` class from the `org.jasypt.util.text` package, which provides similar functionality. I also updated the `setPassword` and `encode` methods to use the new `BasicTextEncryptor` class.

Note that this patch assumes that the rest of the code in the `GeoStorePBEPasswordEncoder` class is unchanged and still works as expected. If that's not the case, additional modifications may be necessary.