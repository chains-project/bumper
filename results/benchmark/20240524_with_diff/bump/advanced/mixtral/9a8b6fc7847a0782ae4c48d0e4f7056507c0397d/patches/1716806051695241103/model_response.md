Here is a fixed version of the `GeoStoreDigestPasswordEncoder` class that uses the new `PasswordEncoder` class from the updated version of the jasypt library:
```java
import org.jasypt.digest.StandardStringDigester;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.AES256TextEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.security.authentication.encoding.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();
    private TextEncryptor textEncryptor = new AES256TextEncryptor();
    private StandardStringDigester digester = new StandardStringDigester();
    private PasswordEncryptor passwordEncryptor = new ConfigurablePasswordEncryptor();

    public GeoStoreDigestPasswordEncoder() {
        this.encryptor.setAlgorithm("PBEWithMD5AndTripleDES");
        this.encryptor.setPassword("password");

        this.textEncryptor.setPassword("password");

        this.digester.setIterations(1024);
        this.digester.setSaltSizeBytes(20);

        this.passwordEncryptor.setAlgorithm("SHA-256");
        this.passwordEncryptor.setIterationCount(1024);
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        if (salt == null) {
            return this.digester.digest(rawPass);
        } else {
            return this.digester.digest(rawPass, (byte[]) salt);
        }
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        if (salt == null) {
            return this.digester.matches(rawPass, encPass);
        } else {
            return this.digester.matches(rawPass, encPass, (byte[]) salt);
        }
    }
}
```
The main changes are:

* The `PBEPasswordEncoder` class has been removed in the updated version of the library, so it has been replaced with the `PasswordEncoder` class.
* The `encryptor`, `textEncryptor`, `digester`, and `passwordEncryptor` fields have been updated to use the new classes from the updated version of the library.
* The `encodePassword` and `isPasswordValid` methods have been updated to use the new `PasswordEncoder` interface.

Note that this is just one possible way to fix the issue. There may be other ways to fix the issue that are more appropriate for your specific use case.