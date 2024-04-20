Here's a fixed version of the client code that uses the new library version:
```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.Pbkdf2PasswordEncoder;

public class GeoStorePBEPasswordEncoder {
    // ...

    private TextEncryptor textEncryptor;
    private PasswordEncoder passwordEncoder;

    public GeoStorePBEPasswordEncoder() {
        PBEStringEncryptor pbeStringEncryptor = new PBEStringEncryptor();
        pbeStringEncryptor.setAlgorithm("PBEWithMD5AndTripleDES");
        pbeStringEncryptor.setPassword("mySalt");

        textEncryptor = pbeStringEncryptor;

        passwordEncoder = new Pbkdf2PasswordEncoder();
    }

    public String encodePassword(String rawPassword) {
        return passwordEncoder.encode(rawPassword);
    }

    public boolean isPasswordValid(String encryptedPassword, String rawPassword) {
        return passwordEncoder.matches(rawPassword, encryptedPassword);
    }

    // ...
}
```
Note that the `PBEPasswordEncoder` class has been removed in the new library version, so we need to use `PBEStringEncryptor` and `TextEncryptor` instead. We also need to use `Pbkdf2PasswordEncoder` from Spring Security to encode and validate passwords.