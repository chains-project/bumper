Here's a possible patch for the client code:
```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    // initialize the encryptor with your secret key
    public GeoStorePBEPasswordEncoder() {
        encryptor.setPassword("your-secret-key");
    }

    public String encode(String rawPassword) {
        return encryptor.encrypt(rawPassword);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return encodedPassword.equals(encryptor.encrypt(rawPassword));
    }
}
```
In this patch, we replaced the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package with the `BasicTextEncryptor` class from the `org.jasypt.util.text` package. We also modified the `GeoStorePBEPasswordEncoder` class to use `BasicTextEncryptor` instead of `PBEPasswordEncoder`.

Note that you need to replace `"your-secret-key"` with your actual secret key.