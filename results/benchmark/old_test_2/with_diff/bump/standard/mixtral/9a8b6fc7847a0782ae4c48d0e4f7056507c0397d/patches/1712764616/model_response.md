Here's the proposed patch:
```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.Pbkdf2PasswordEncoder;

// ...

private TextEncryptor textEncryptor = new PBEStringEncryptor();
private PasswordEncoder passwordEncoder = new Pbkdf2PasswordEncoder();

// ...

public String encodePassword(String rawPassword, Object salt) {
    return passwordEncoder.encode(rawPassword);
}

public boolean isPasswordValid(String encoderPassword, String rawPassword, Object salt) {
    return passwordEncoder.matches(rawPassword, encoderPassword);
}
```
Explanation:
Since the `org.jasypt.spring.security.PBEPasswordEncoder` class is no longer available, we need to find an alternative way to encode and validate passwords. In this case, we can use the `org.springframework.security.crypto.password.PasswordEncoder` interface, which provides similar functionality.
We can use `Pbkdf2PasswordEncoder` as the concrete implementation of `PasswordEncoder`.
For the `encodePassword` method, we can directly use the `encode` method provided by `Pbkdf2PasswordEncoder`.
For the `isPasswordValid` method, we can use the `matches` method provided by `Pbkdf2PasswordEncoder` to check if the raw password matches the encoded password.
Note that the `salt` parameter is not used in this implementation, as the `Pbkdf2PasswordEncoder` does not require a salt parameter for encoding or validation. If a salt is required, a different implementation of `PasswordEncoder` may need to be used.