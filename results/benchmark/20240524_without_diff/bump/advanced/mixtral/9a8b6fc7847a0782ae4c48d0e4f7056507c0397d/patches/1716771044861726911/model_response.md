Here's a proposed patch for the given client code:
```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    // ...
    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    // ...
    @Override
    public String encode(CharSequence rawPassword) {
        // ...
        encryptor.setPassword(salt);
        String encryptedPassword = encryptor.encrypt(rawPassword.toString());
        // ...
        return encryptedPassword;
    }
    // ...
}
```
This patch replaces the usage of `PBEPasswordEncoder` from the `org.jasypt.spring.security` package with `BasicTextEncryptor` from the `org.jasypt.util.text` package. The `encode` method is updated accordingly. Note that this patch assumes that the `salt` variable is defined and available in the class.