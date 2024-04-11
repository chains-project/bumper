Here is a fixed version of the failing method using the new library version:

```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.Pbkdf2PasswordEncoder;

//...

private PasswordEncoder passwordEncoder = new PasswordEncoder() {
    private TextEncryptor textEncryptor = new StandardPBEStringEncryptor();
    (...)
    @Override
    public String encode(CharSequence rawPassword) {
        return new Pbkdf2PasswordEncoder().encode(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return new Pbkdf2PasswordEncoder().matches(rawPassword.toString(), encodedPassword);
    }
};
```

This version uses the new classes and methods added in the new library version, such as `TextEncryptor`, `PBEStringEncryptor`, `PasswordEncoder`, and `Pbkdf2PasswordEncoder`. It also removes the usage of the deprecated `PBEPasswordEncoder` class and its methods.