Here is the updated code that uses the new class and method names:
```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;

//...

private final TextEncryptor textEncryptor = new org.jasypt.contrib.org.bouncycastle.BouncyCastleStringEncryptor();
private final PasswordEncryptor passwordEncryptor = new PasswordEncrypts();
private final PasswordEncoder passwordEncoder = new PasswordEncoder() {
    @Override
 
   public String encode(CharSequence rawPassword) {
        return passwordEncryptor.encryptPassword(rawPassword.toString());
    }

    @Override
    public boolean matches(CharSequence rawPassword, String encodedPassword) {
        return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
    }
};

//...
```
Note that the `TextEncryptor` and `PasswordEncryptor` classes have been moved from the `org.jasypt.spring.security` package to the `org.jasypt.util` package. Also, the `PasswordEncoder` class has been moved from the `org.jasypt.spring.security` package to the `org.springframework.security.crypto.password` package.

Additionally, the `PBEPasswordEncoder` class has been replaced with the `PasswordEncryptor` and `PasswordEncoder` classes. The `textEncryptor` and `passwordEncryptor` objects can be used to encrypt and decrypt strings, and the `passwordEncoder` object can be used to encode and verify passwords.

Finally, the `isPasswordValid` method has been replaced with the `matches` method in the `PasswordEncoder` class.

I hope this helps! Let me know if you have any questions.