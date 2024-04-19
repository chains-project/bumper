Here's a proposed patch to fix the error:
```java
import org.jasypt.spring.security.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {
    private PasswordEncoder passwordEncoder;

    public GeoStoreDigestPasswordEncoder() {
        passwordEncoder = new org.jasypt.spring.security.PBEPasswordEncoder();
    }

    @Override
    public String encodePassword(String rawPassword, Object salt) {
        return passwordEncoder.encodePassword(rawPassword, salt);
    }

    @Override
    public boolean isPasswordValid(String rawPassword, String encodedPassword, Object salt) {
        return passwordEncoder.isPasswordValid(rawPassword, encodedPassword, salt);
    }

    @Override
    public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
        passwordEncoder.setPasswordEncryptor(passwordEncryptor);
    }

    @Override
    public void setStringDigester(StringDigester stringDigester) {
        passwordEncoder.setStringDigester(stringDigester);
    }
}
```
In this patch, we've removed the `PBEPasswordEncoder` constructor and instead created a `PasswordEncoder` instance using the `org.jasypt.spring.security.PBEPasswordEncoder` class. We've also removed the `setPbeStringEncryptor` and `setTextEncryptor` methods as they are no longer available in the new version of the library. Finally, we've added the `setPasswordEncryptor` and `setStringDigester` methods to match the new API.

Note that this patch assumes that the `org.jasypt.spring.security.PBEPasswordEncoder` class is still available in the new version of the library. If that class has been removed, you may need to use a different implementation of `PasswordEncoder`.