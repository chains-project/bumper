Sure, here' cooperating with the new version of the library, the `GeoStoreDigestPasswordEncoder` class can be modified as follows:

```java
import org.jasypt.util.password.BasicPasswordEncryptor;
import org.springframework.security.authentication.encoding.PasswordEncoder;

public class GeoStoreDigestPasswordEncoder implements PasswordEncoder {

    private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncrypt

```

    @Override
    public String encodePassword(String rawPass, Object salt) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    @Override
    public boolean isPasswordValid(String encPass, String rawPass, Object salt) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}

```

This code uses the `BasicPasswordEncryptor` class from the updated version of the library to handle the password encoding and validation.

The `encodePassword` and `isPasswordValid` methods have been updated accordingly to use the new `BasicPasswordEncryptor` instance.

Note that the `salt` parameter is not used in this example, but you can modify the code as needed to incorporate it.

I hope this helps! Let me know if you have any questions.