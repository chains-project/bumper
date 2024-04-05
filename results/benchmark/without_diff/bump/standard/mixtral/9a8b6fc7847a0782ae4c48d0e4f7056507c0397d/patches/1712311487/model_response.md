Here's the patched version of the method using the new library method `new BCryptPasswordEncoder()` from the added library `org.springframework.security.crypto.bcrypt`.

```java
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;

//...

@Bean
public PasswordEncoder passwordEncoder() {
    return new BCryptPasswordEncoder();
}
```