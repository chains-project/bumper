Here is the proposed patch:

```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.jasypt.digest.StringDigester;
import org.springframework.security.crypto.password.PasswordEncoder;

// ...

private PasswordEncoder passwordEncoder;

// ...

public void setTextEncryptor(TextEncryptor textEncryptor) {
    PBEStringEncryptor pbeStringEncryptor = new PBEStringEncryptor();
    pbeStringEncryptor.setAlgorithm("PBEWithMD5AndTripleDES");
    pbeStringEncryptor.setPassword(textEncryptor.decrypt("ENCRYPT_PASSWORD"));
    passwordEncoder = new PasswordEncoder() {
        @Override
        public String encode(CharSequence rawPassword) {
            return pbeStringEncryptor.encryptPassword(rawPassword.toString());
        }

        @Override
        public boolean matches(CharSequence rawPassword, String encodedPassword) {
            return pbeStringEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
        }
    };
}

// Use passwordEncoder instead of the old PBEPasswordEncoder
```

This patch creates a new `PasswordEncoder` instance that uses a `PBEStringEncryptor` under the hood. The `setTextEncryptor` method is used to initialize the `PBEStringEncryptor` with the necessary encryption settings. The `PasswordEncoder` instance can then be used to encode and validate passwords.