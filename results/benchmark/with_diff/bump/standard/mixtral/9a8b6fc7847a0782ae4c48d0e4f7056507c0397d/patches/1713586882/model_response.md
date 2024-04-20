Here's the patched version of the failing method in GeoStorePBEPasswordEncoder.java:
```java
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.ConfigurablePasswordEncryptor;
import org.springframework.security.authentication.encoding.PasswordEncoder;

//...

private PasswordEncoder passwordEncoder = new PasswordEncoder() {
    private TextEncryptor textEncryptor = new StandardPBEStringEncryptor();
    private ConfigurablePasswordEncryptor passwordEncryptor = new ConfigurablePasswordEncryptor();

    {
        textEncryptor.setAlgorithm("PBEWithMD5AndTripleDES");
        textEncryptor.setPassword(geostoreProperties.getEncryptionPassword());

        passwordEncryptor.setAlgorithm(textEncryptor.getAlgorithm());
        passwordEncryptor.setPassword(textEncryptor.getPassword());
    }

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return textEncryptor.encrypt(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
};
```
The patch creates a custom `PasswordEncoder` implementation by extending the `PasswordEncoder` interface directly. It also initializes a `TextEncryptor` and a `ConfigurablePasswordEncryptor` for encryption and validation accordingly. The `encodePassword` and `isPasswordValid` methods are implemented using the new encryptor and password encryptor objects.