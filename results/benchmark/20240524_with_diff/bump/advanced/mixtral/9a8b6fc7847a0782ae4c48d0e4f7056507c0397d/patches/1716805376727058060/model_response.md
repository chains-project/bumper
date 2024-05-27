Here's a possible patch for the failing client code:
```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.Pbkdf2PasswordEncoder;

public class GeoStorePBEPasswordEncoder {
    // ...

    private PasswordEncoder passwordEncoder;

    public GeoStorePBEPasswordEncoder() {
        TextEncryptor textEncryptor = new TextEncryptor();
        textEncryptor.setPassword("my-secret-key");

        PBEStringEncryptor pbeEncryptor = new PBEStringEncryptor();
        pbeEncryptor.setAlgorithm("PBEWithMD5AndTripleDES");
        pbeEncryptor.setPassword("my-secret-key");
        textEncryptor.setStringEncryptor(pbeEncryptor);

        this.passwordEncoder = new Pbkdf2PasswordEncoder();
        this.passwordEncoder.setEncodeHashAsBase64(true);
        this.passwordEncoder.setIterations(1000);
        this.passwordEncoder.setKeySize(128);
        this.passwordEncoder.setStringEncryptor(textEncryptor);
    }

    public String encodePassword(String rawPassword, Object salt) {
        return this.passwordEncoder.encode(rawPassword);
    }

    public boolean isPasswordValid(String encryptedPassword, String rawPassword, Object salt) {
        return this.passwordEncoder.matches(rawPassword, encryptedPassword);
    }

    // ...
}
```
The patch creates a new `PasswordEncoder` instance from `org.springframework.security.crypto.password` package, and sets it as a member variable.
It then sets the `StringEncryptor` for the `TextEncryptor` instance, which is then set as the `StringEncryptor` for the `PasswordEncoder` instance.
The `encodePassword` and `isPasswordValid` methods are updated to use the new `PasswordEncoder` instance.
Note that the `salt` parameter is not used in this implementation, but it can be added if needed.