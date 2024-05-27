Here's the patched method:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    // ...

    @Autowired
    public GeoStoreDigestPasswordEncoder(GeoStorePasswordPolicy passwordPolicy) {
        this.passwordPolicy = passwordPolicy;
        this.passwordEncryptor = new BasicPasswordEncryptor();
    }

    // ...
}
```
In this patched method, I replaced the dependency on `org.jasypt.spring.security.PasswordEncoder` with `org.jasypt.util.password.BasicPasswordEncryptor`. This allows the code to continue functioning without relying on the problematic package.