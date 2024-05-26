Here is the updated version of the `GeoStoreDigestPasswordEncoder` class that uses the new version of the `org.jasypt.spring.security.PasswordEncoder` class:
```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.spring.security.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder {
    // ...

    private PasswordEncoder passwordEncoder;

    public GeoStoreDigestPasswordEncoder() {
        // Create a new instance of the updated PasswordEncoder
        PasswordEncoder pe = new PasswordEncoder() {
            private final PasswordEncryptor passwordEncryptor = new PasswordEncrypts();

            @Override
            public String encodePassword(String rawPass, Object salt) {
                return passwordEncryptor.encryptPassword(rawPass);
            }

            @Override
            public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
                return passwordEncryptor.checkPassword(rawPass, encPass);
            }

            @Override
g            public void setPasswordEncryptor(PasswordEncryptor passwordEncryptor) {
                throw new UnsupportedOperationException("Not supported yet.");
            }

            @Override
            public void setStringDigester(StringDigester stringDigester) {
                throw new UnsupportedOperationException("Not supported yet.");
            }
        };

        // Create a new instance of the PBEStringEncryptor and set it to the PasswordEncoder
        PBEStringEncryptor pbe = new PBEStringEncryptor();
        pbe.setPassword(salt);
        pe.setTextEncryptor(pbe);

        // Set the updated PasswordEncoder to the class
        this.passwordEncoder = pe;
    }

    // ...
}
```
The changes in this updated version include:

* Importing the new classes `PBEStringEncryptor`, `TextEncryptor`, and `PasswordEncryptor` from the `org.jasypt.util` and `org.jasypt.encryption.pbe` packages
* Creating a new instance of the updated `PasswordEncoder` class
* Creating a new instance of the `PBEStringEncrypt` class and setting it as the `TextEncryptor` for the `PasswordEncoder`
* Setting the `salt` as the password for the `PBEStringEncryptor`
* Removing the `org.jasypt.spring.security.PBEPasswordEncoder` class, as it has been removed in the new version
* Implementing the `encodePassword`, `isPasswordValid`, `setPasswordEncryptor`, and `setStringDigester` methods in the anonymous inner class that extends `PasswordEncoder`

I hope this helps! Let me know if you have any questions.