Here's the patched method:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    // ...

    @Autowired
    public GeoStoreDigestPasswordEncoder(final GeoStoreSecurityProperties securityProperties) {
        this.securityProperties = securityProperties;
        this.passwordEncryptor = new BasicPasswordEncryptor();
    }

    // ...
}
```
This patch replaces the `PasswordEncoder` from `org.jasypt.spring.security` with `BasicPasswordEncryptor` from `org.jasypt.util.password`.

The `PasswordEncoder` interface from `org.jasypt.spring.security` is now deprecated and removed in newer versions of jasypt.
`BasicPasswordEncryptor` from `org.jasypt.util.password` can be used as a replacement for basic password encoding functionality.

Please note that this might not be a drop-in replacement if more advanced features of the `PasswordEncoder` interface were used.