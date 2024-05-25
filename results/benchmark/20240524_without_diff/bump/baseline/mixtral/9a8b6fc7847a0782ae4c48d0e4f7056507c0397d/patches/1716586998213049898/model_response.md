Here's a potential patch for the issue you're facing:

```java
import org.jasypt.util.password.DigestPasswordEncoder;

@Override
public PasswordEncoder passwordEncoder() {
    DigestPasswordEncoder encoder = new DigestPasswordEncoder();
    encoder.setAlgorithm("SHA-256");
    return encoder;
}
```

In this patch, we've replaced the org.jasypt.spring.security package with org.jasypt.util.password, and DigestPasswordEncoder is used instead of PasswordEncoder. The algorithm is set to SHA-256 to ensure compatibility with the previous implementation.