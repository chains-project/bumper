Here's a possible patch for the code:

```java
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

@Override
protected PasswordEncoder createStringEncoder() {
    return new BCryptPasswordEncoder();
}
```

This code creates a new `BCryptPasswordEncoder` instance, which is a password encoder that uses the BCrypt hashing algorithm. This should fix the "cannot find symbol" error by replacing the old `PasswordEncoder` implementation with a new one that is available in the current version of the external dependency.