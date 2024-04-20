Here's the fixed version of the failing method in `GeoStorePBEPasswordEncoder.java`:
```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.text.BasicTextEncryptor;
import org.springframework.security.authentication.encoding.PasswordEncoder;
import org.springframework.security.authentication.encoding.PlaintextPasswordEncoder;

// ...

private PasswordEncoder passwordEncoder = new PasswordEncoder() {
    private TextEncryptor textEncryptor = new BasicTextEncryptor();
    private StandardPBEStringEncryptor encryptor = new StandardPBEStringEncryptor();

    {
        textEncryptor.setPassword(geostoreProperties.getEncryptionPassword());
        encryptor.setPassword(geostoreProperties.getEncryptionPassword());
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return textEncryptor.encrypt(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return encPass.equals(textEncryptor.encrypt(rawPass));
    }
};
```
This version uses the new classes and methods available in the updated library. The `PBEPasswordEncoder` class has been replaced with `PasswordEncoder` and `TextEncryptor`. Also, the encryption is now done using `BasicTextEncryptor` and `StandardPBEStringEncryptor`. The `encodePassword` and `isPasswordValid` methods have been updated accordingly.