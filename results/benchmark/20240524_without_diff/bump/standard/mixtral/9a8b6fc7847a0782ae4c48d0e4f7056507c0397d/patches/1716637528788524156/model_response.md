Here's a proposed patch that you can apply to the client code to fix the error:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

// ...

public class GeoStoreDigestPasswordEncoder {

    private BasicPasswordEncryptor encryptor = new BasicPasswordEncryptor();

    // ...

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encryptPassword(rawPassword.toString());
    }

    // ...

}
```
This patch replaces the dependency on `org.jasypt.spring.security.PasswordEncoder` with `org.jasypt.util.password.BasicPasswordEncryptor`, which provides similar functionality for password encryption. The `encode` method has been updated to use the new encryptor.