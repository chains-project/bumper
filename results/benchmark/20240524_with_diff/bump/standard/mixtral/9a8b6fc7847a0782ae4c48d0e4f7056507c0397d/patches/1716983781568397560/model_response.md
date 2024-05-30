Here is the proposed patch:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.AES256TextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.StandardPasswordEncoder;

public class GeoStoreDigestPasswordEncoder {
    private PasswordEncoder passwordEncoder;

    public GeoStoreDigestPasswordEncoder() {
        TextEncryptor textEncryptor = new AES256TextEncryptor();
        textEncryptor.setPassword("your-secret-key");
        BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();
        passwordEncryptor.setAlgorithm("SHA-256");
        passwordEncoder = new StandardPasswordEncoder(textEncryptor, passwordEncryptor);
    }

    public String encodePassword(String rawPassword) {
        return passwordEncoder.encode(rawPassword);
    }

    public boolean isPasswordValid(String encryptedPassword, String rawPassword) {
        return passwordEncoder.matches(rawPassword, encryptedPassword);
    }
}
```
Explanation:
The `PBEPasswordEncoder` class has been removed in the new version of the library. Instead, we can use the `PasswordEncoder` interface from the `org.springframework.security.crypto.password` package. We can create an instance of `StandardPasswordEncoder` and set the text and password encryptors. We can then use the `encode` and `matches` methods of the `PasswordEncoder` interface to encode and validate passwords.
Note: You need to replace "your-secret-key" with your actual secret key.