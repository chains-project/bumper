Here is the updated version of the failing client code that should work with the new version of the library:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder {

    private final PasswordEncoder passwordEncoder;

    public GeoStoreDigestPasswordEncoder() {
        this.passwordEncoder = new BasicPasswordEncryptor();
    }

    public String encode(String rawPassword) {
        return passwordEncoder.encode(rawPassword);
}

    public boolean matches(String rawPassword, String encodedPassword) {
        return passwordEncoder.matches(rawPassword, encodedPassword);
    }
}
```
In the updated code, I have replaced the `org.jasypt.spring.security` package with `org.jasypt.util.password` and `org.springframework.security.crypto.password` packages. I have also replaced the `PBEPasswordEncoder` class with the `BasicPasswordEncryptor` class from the `org.jasypt.util.password` package.

The `BasicPasswordEncryptor` class provides similar functionality to the `PBEPasswordEncoder` class and can be used to encode and check passwords.

The `PasswordEncoder` interface from the `org.springframework.security.crypto.password` package has been added to the import statements and is being used to ensure compatibility with Spring Security.

Note that the `GeoStoreDigestPasswordEncoder` class still adheres to the same function signature and does not require any changes to the external code that uses it.