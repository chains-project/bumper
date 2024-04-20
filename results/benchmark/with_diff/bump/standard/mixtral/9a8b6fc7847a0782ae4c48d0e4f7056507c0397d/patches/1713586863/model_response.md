Here's a fixed version of the failing method using the new library version:
```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.BasicTextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.Pbkdf2PasswordEncoder;

//...

private PasswordEncoder passwordEncoder;

//...

@PostConstruct
public void init() {
    TextEncryptor textEncryptor = new BasicTextEncryptor();
    textEncryptor.setPassword(ENCRYPTION_PASSWORD);
    passwordEncoder = new Pbkdf2PasswordEncoder(ENCRYPTION_STRENGTH, textEncryptor);
}

public String encodePassword(String rawPassword) {
    return passwordEncoder.encode(rawPassword);
}

public boolean isPasswordValid(String encryptedPassword, String rawPassword) {
    return passwordEncoder.matches(rawPassword, encryptedPassword);
}
```
This version replaces the usage of `PBEPasswordEncoder` with `Pbkdf2PasswordEncoder` from the `org.springframework.security.crypto.password` package. The `TextEncryptor` interface is used for encryption and decryption in combination with `Pbkdf2PasswordEncoder`. The `isPasswordValid` method is implemented using the `matches` method from `Pbkdf2PasswordEncoder`.