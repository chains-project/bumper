Here's a possible patch for the failing client code:

```java
import org.jasypt.util.password.DigestPasswordEncoder;

public class GeoStoreDigestPasswordEncoder {

    private DigestPasswordEncoder passwordEncoder;

    @Override
    public void afterPropertiesSet() throws Exception {
        this.passwordEncoder = new DigestPasswordEncoder("SHA-256", 1024);
    }

    @Override
    public String encodePassword(String rawPass, Object salt) throws Exception {
        return passwordEncoder.encodePassword(rawPass, (String) salt);
    }

    @Override
    public boolean matches(String encPass, String rawPass, Object salt) throws Exception {
        return passwordEncoder.matches(encPass, rawPass, (String) salt);
    }

}
```

In this patch, we replace the `PasswordEncoder` class from `org.jasypt.spring.security` with the `DigestPasswordEncoder` class from `org.jasypt.util.password`. This class provides similar functionality for encoding and matching passwords. We also update the import statements accordingly.

Note that this patch assumes that the `PasswordEncoder` interface and its methods have not changed significantly in the new version. If there are any changes, further modifications may be necessary.