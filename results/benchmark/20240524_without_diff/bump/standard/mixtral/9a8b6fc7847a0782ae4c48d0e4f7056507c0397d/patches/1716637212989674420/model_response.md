```java
import org.jasypt.password.PBEPasswordEncoder;

// Change the following line
// PBEPasswordEncoder encoder = new PBEPasswordEncoder();
// to
PBEPasswordEncoder encoder = new PBEPasswordEncoder(new StandardPBEStringEncryptor());
```

This patch replaces the `org.jasypt.spring.security.PBEPasswordEncoder` with `org.jasypt.password.PBEPasswordEncoder` and initializes it with a new `StandardPBEStringEncryptor` instance. This should fix the failure caused by the missing `org.jasypt.spring.security` package.