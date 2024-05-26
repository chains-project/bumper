Here is the patched code:

```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePasswordEncoder {
    private StrongPasswordEncryptor passwordEncryptor;

    public GeoStorePasswordEncoder() {
        this.passwordEncryptor = new StrongPasswordEncryptor();
    }

    public String encodePassword(String password, Object salt) {
        return passwordEncryptor.encryptPassword(password);
    }

    public boolean isPasswordValid(String encodedPassword, String password, Object salt) {
        return passwordEncryptor.checkPassword(password, encodedPassword);
    }
}
```