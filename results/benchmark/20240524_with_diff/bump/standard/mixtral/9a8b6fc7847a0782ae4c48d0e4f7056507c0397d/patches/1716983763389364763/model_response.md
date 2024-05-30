Here is the proposed patch for the failing client code:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.TextEncryptorFactory;
import org.springframework.security.crypto.password.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder {

    private TextEncryptor textEncryptor;
    private BasicPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        this.textEncryptor = TextEncryptorFactory.createTextEncryptor();
        this.passwordEncryptor = new BasicPasswordEncryptor();
    }

    public String encodePassword(String rawPass, Object salt) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }

    public void setPasswordEncryptor(PasswordEncoder passwordEncoder) {
        // Not needed in this implementation
    }

    public void setTextEncryptor(TextEncryptor textEncryptor) {
        this.textEncryptor = textEncryptor;
    }
}
```

In this patch, I have replaced the deprecated `org.jasypt.spring.security` package with the equivalent classes from the `org.jasypt.util` and `org.springframework.security.crypto.password` packages. I have also created a `TextEncryptor` instance in the constructor and added a new setter method for it. The `PasswordEncoder` interface has been added to allow for future compatibility if needed, but it is not used in this implementation.

Note that I have assumed that the `salt` parameter is not being used in this implementation, as it was not used in the original code and there were no methods available in the new library version that accept a salt parameter. If the salt parameter is required, you may need to modify this implementation accordingly.