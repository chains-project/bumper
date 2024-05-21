Sure, I understand that you need a fixed version of the `GeoStorePBEPasswordEncoder` class that uses the new version of the library. Here is the fixed version of the method:
```java
import org.jasypt.encryption.pbe.PBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;
import org.jasypt.util.password.PasswordEncryptor;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Component;

import it.geosolutions.geostore.core.security.password.GeoStorePasswordEncoder;

@Component
public class GeoStorePBEPasswordEncoder extends GeoStorePasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
        // configure the encryptors here
        PBEStringEncryptor pbeStringEncryptor = new PBEStringEncryptor();
        pbeStringEncryptor.setAlgorithm("PBEWithMD5AndTripleDES");
        pbeStringEncryptor.setPassword("myPassword");

        TextEncryptor textEncryptor = new TextEncryptor();
        textEncryptor.setPassword("myPassword");

        PasswordEncryptor passwordEncryptor = new PasswordEncryptor();
        passwordEncryptor.setAlgorithm("SHA-1");
        passwordEncryptor.setPlainDigest(false);

        setPbeStringEncryptor(pbeStringEncryptor);
        setTextEncryptor(textEncryptor);
        setPasswordEncryptor(passwordEncryptor);

        setEncoder(new PasswordEncoder() {

            @Override
            public String encode(CharSequence rawPassword) {
                return passwordEncryptor.encryptPassword(rawPassword.toString());
            }

            @Override
            public boolean matches(CharSequence rawPassword, String encodedPassword) {
                return passwordEncryptor.checkPassword(rawPassword.toString(), encodedPassword);
            }
        });
    }
}
```
In this new version, I have replaced the `PBEPasswordEncoder` class with the `PasswordEncoder` class, which has the same methods as the old `PBEPasswordEncoder` class. I have also added the necessary imports for the new classes.

Note that you will need to configure the `PBEStringEncryptor`, `TextEncryptor`, and `PasswordEncryptor` objects with the appropriate values for your use case.

I hope this helps! Let me know if you have any questions.