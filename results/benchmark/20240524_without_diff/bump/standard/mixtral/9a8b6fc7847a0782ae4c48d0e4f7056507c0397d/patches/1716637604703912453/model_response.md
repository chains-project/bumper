Here's a proposed patch for the client code:
```java
import org.jasypt.digest.StandardStringDigester;

public class GeoStoreDigestPasswordEncoder {
    private StandardStringDigester digester;

    public GeoStoreDigestPasswordEncoder() {
        this.digester = new StandardStringDigester();
        this.digester.setAlgorithm("SHA-256");
    }

    public String encode(String rawPassword) {
        return this.digester.digest(rawPassword);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return encodedPassword.equals(this.digester.digest(rawPassword));
    }
}
```
In this patch, we have replaced the `org.jasypt.spring.security.PasswordEncoder` interface with the `org.jasypt.digest.StandardStringDigester` class from the same library. This allows us to continue using the library's digest functionality without relying on the `org.jasypt.spring.security` package.

Note that we have also updated the constructor and `matches` method to use the new `StandardStringDigester` class. The `encode` method remains unchanged.

Overall, this patch should allow the client code to continue using the jasypt library for password digestion, even if the `org.jasypt.spring.security` package is no longer available.