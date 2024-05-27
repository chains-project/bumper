Here's a fixed version of the `GeoStoreDigestPasswordEncoder` class that uses the new `PasswordEncoder` class from the updated library:
```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.security.authentication.encoding.PasswordEncoder;
import org.springframework.security.crypto.password.StandardPasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private final PasswordEncoder passwordEncoder;

    public GeoStoreDigestPasswordEncoder() {
        PasswordEncryptor passwordEncryptor = new PasswordEncryptor();
        PBEStringEncryptor pbeStringEncryptor = new PBEStringEncryptor();
        TextEncryptor textEncryptor = new TextEncryptor();
        textEncryptor.setPasswordEncryptor(passwordEncryptor);
        pbeStringEncryptor.setPassword(passwordEncryptor.encryptPassword("geostore", "salt"));
        passwordEncryptor.setAlgorithm("SHA-256");
        passwordEncryptor.setIterationCount(1024);
        passwordEncryptor.setKeyObtentionIterations(1024);
        passwordEncryptor.setPoolSize(1);
        passwordEncryptor.setProviderName("SunJCE");
        passwordEncryptor.setSaltGenerator(new RandomSaltGenerator());
        this.passwordEncoder = new StandardPasswordEncoder();
        this.passwordEncoder.setPasswordEncoder(passwordEncryptor);
        this.passwordEncoder.setEncryptor(passwordEncryptor);
        this.passwordEncoder.setTextEncryptor(textEncryptor);
        this.passwordEncoder.setPbeStringEncryptor(pbeStringEncryptor);
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return passwordEncoder.encodePassword(rawPass, salt);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncoder.isPasswordValid(encPass, rawPass, salt);
    }
}
```
The changes made include:

* Importing the new `PasswordEncoder` class from the updated library.
* Creating new instances of `PasswordEncryptor`, `PBEStringEncryptor`, and `TextEncryptor` classes from the updated library.
* Setting the properties of the `PasswordEncryptor` instance, such as the algorithm, iteration count, and salt generator.
* Creating a new instance of `StandardPasswordEncoder` and setting its password encoder, encryptor, text encryptor, and PBE string encryptor to the corresponding instances created earlier.
* Overriding the `encodePassword` and `isPasswordValid` methods of the `PasswordEncoder` interface to use the new `passwordEncoder` instance.