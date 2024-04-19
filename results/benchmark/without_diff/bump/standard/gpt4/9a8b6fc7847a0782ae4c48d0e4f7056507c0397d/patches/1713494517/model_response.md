It seems like the library `org.jasypt.spring.security.PBEPasswordEncoder` is not available anymore. You can use `org.springframework.security.crypto.password.Pbkdf2PasswordEncoder` instead. Here is the corrected import statement:

```java
import org.springframework.security.crypto.password.Pbkdf2PasswordEncoder;
```