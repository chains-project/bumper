Here is the updated code for the `GeoStorePBEPasswordEncoder` class that uses the new `PasswordEncoder` class from the updated version of the library:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStorePBEPasswordEncoder {

    private PasswordEncoder passwordEncoder;

    public GeoGeoStorePBEPasswordEncoder() {
        BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();
        this.passwordEncoder = new StandardPasswordEncoder(passwordEncryptor);
    }

    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncoder.encode(rawPassword);
    }

    public boolean isPasswordValid(String rawPassword, String encodedPassword, Object salt) {
        return passwordEncoder.matches(rawPassword, encodedPassword);
    }
}
```
In this updated code, we are using the `PasswordEncoder` interface from the `org.springframework.security.crypto.password` package to encode and verify passwords. We are using the `BasicPasswordEncryptor` class from the `org.jasypt.util.password` package to create an instance of `PasswordEncoder`.

Note that the `isPasswordValid` method has been updated to use the `matches` method of the `PasswordEncoder` interface instead of the `isPasswordValid` method of the `PBEPasswordEncoder` class.

Also note that the `setPasswordEncryptor` and `setStringDigester` methods have been removed from the updated version of the library, so they are not used in this updated code.