Here's a possible patch to fix the error:
```java
@Override
protected PasswordEncoder createStringEncoder() {
    PasswordEncoder encoder = new PasswordEncoder();
    encoder.setPasswordEncryptor(new StrongPasswordEncryptor());
    return encoder;
}
```
Note that I replaced the fully qualified class names with their simple names, assuming that the necessary imports are already in place. If that's not the case, you can add the following imports:
```java
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.password.StrongPasswordEncryptor;
```
The `PasswordEncoder` interface was added in Spring Security 5, which might be the source of the compatibility issue. The `StrongPasswordEncryptor` class is part of the Jasypt library, and it should still be compatible with the new version of Spring Security.