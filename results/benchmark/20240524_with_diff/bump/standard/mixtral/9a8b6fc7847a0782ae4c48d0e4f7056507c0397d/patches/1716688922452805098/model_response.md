Here is a possible fix for the failing client code:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder {

    private final PasswordEncoder passwordEncoder = new PasswordEncoder() {
        private final BasicPasswordEncryptor basicPasswordEncryptor = new BasicPasswordEncryptor();

        @Override
        public String encode(CharSequence rawPassword) {
            return basicPasswordEncryptor.encryptPassword(rawPassword.toString());
        }

        @Override
        public boolean matches(CharSequence rawPassword, String encodedPassword) {
            return basicPasswordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
        }
    };

    // rest of the class
}
```
In this solution, we replace the `org.jasypt.spring.security.PasswordEncoder` with `org.springframework.security.crypto.password.PasswordEncoder` and use `org.jasypt.util.password.BasicPasswordEncryptor` to implement the required functionality.

Note that this solution assumes that the `BasicPasswordEncryptor` provides compatible behavior with the previous `PBEPasswordEncoder`. If not, further modifications may be needed.