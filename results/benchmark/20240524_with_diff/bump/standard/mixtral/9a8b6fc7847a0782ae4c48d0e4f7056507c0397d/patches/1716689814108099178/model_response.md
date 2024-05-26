Here is a fixed version of the failing method in GeoStoreDigestPasswordEncoder.java:

```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.security.authentication.encoding.PasswordEncoder;

// ...

private PasswordEncoder passwordEncoder = new PasswordEncoder() {
    private TextEncryptor textEncryptor = new ConfigurablePasswordEncryptor();

    @Override
    public String encodePassword(String rawPass, Object salt) {
        textEncryptor.setPassword(salt.toString());
        return textEncryptor.encrypt(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        textEncryptor.setPassword(salt.toString());
        return textEncryptor.checkPassword(rawPass, encPass);
    }
};
```

Changes made:

* Imported required classes for `TextEncryptor`, `ConfigurablePasswordEncryptor`, and `PasswordEncryptor`.
* Created an anonymous implementation of `PasswordEncoder` interface.
* Created a `TextEncryptor` instance for password encryption and validation.
* Implemented `encodePassword` and `isPasswordValid` methods of `PasswordEncoder` interface.
* Removed dependency on `org.jasypt.spring.security` package.