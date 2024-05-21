Here is a fixed version of the failing method that uses the new library version:

```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.crypto.password.Pbkdf2PasswordEncoder;

//...

private PasswordEncoder passwordEncoder;

//...

passwordEncoder = new Pbkdf2PasswordEncoder();
```

Note that `PBEPasswordEncoder` has been replaced with `Pbkdf2PasswordEncoder`, which is a subclass of `PasswordEncoder`. Additionally, `TextEncryptor` and `PBEStringEncryptor` are used instead of the removed methods from `PBEPasswordEncoder`.