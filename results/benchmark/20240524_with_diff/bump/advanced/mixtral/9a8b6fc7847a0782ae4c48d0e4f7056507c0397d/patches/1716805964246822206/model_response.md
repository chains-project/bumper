Here's the proposed patch:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.TextEncryptorFactory;
import org.springframework.security.authentication.encoding.PasswordEncoder;
import org.springframework.security.authentication.encoding.PlaintextPasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private TextEncryptor textEncryptor;
    private BasicPasswordEncryptor passwordEncryptor;

    public GeoStoreDigestPasswordEncoder() {
        this.textEncryptor = TextEncryptorFactory.createTextEncryptor();
        this.passwordEncryptor = new BasicPasswordEncryptor();
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        if (salt == null) {
            return this.passwordEncryptor.encryptPassword(rawPass);
        } else {
            return this.textEncryptor.encrypt(rawPass);
        }
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        if (salt == null) {
            return this.passwordEncryptor.checkPassword(rawPass, encPass);
        } else {
            String newEncPass = this.encodePassword(rawPass, salt);
            return newEncPass.equals(encPass);
        }
    }
}
```
Explanation:
Since the `org.jasypt.spring.security` package has been removed, we need to import the necessary classes from `org.jasypt.util` and `org.springframework.security.authentication.encoding` packages.
I have created two objects `textEncryptor` and `passwordEncryptor` for encryption and password validation respectively.
The `encodePassword` method checks if the salt is null or not, if it's null, it encrypts the password using `passwordEncryptor` and if it's not null, it encrypts the password using `textEncryptor`.
The `isPasswordValid` method checks if the salt is null or not, if it's null, it validates the password using `passwordEncryptor` and if it's not null, it encrypts the raw password using `encodePassword` method and checks if it's equal to the encrypted password.