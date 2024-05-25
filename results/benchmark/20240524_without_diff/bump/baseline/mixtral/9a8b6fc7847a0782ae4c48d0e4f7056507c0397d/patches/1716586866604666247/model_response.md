Here's the proposed patch for the failing client code:

```java
import org.jasypt.util.password.StrongPasswordEncryptor;

@Component
public class GeoStoreDigestPasswordEncoder extends PasswordEncoder {

    private final StrongPasswordEncryptor encryptor = new StrongPasswordEncryptor();

    @Override
    public String encode(CharSequence rawPassword) {
        return encryptor.encryptPassword(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
}
```

Note that we replaced the import statement for `PasswordEncoder` with `StrongPasswordEncryptor` from the `org.jasypt.util.password` package. We also updated the method implementations to use the new `StrongPasswordEncryptor` methods.