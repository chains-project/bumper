Here is a possible patch for the failing client code:
```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    // initialize the encryptor with your desired properties
    public GeoStorePBEPasswordEncoder() {
        encryptor.setPassword("my-secret-password");
    }

    public String encode(String rawPassword) {
        return encryptor.encrypt(rawPassword);
    }

    public boolean matches(String rawPassword, String encodedPassword) {
        return encryptor.checkPassword(rawPassword, encodedPassword);
    }
}
```
This patch replaces the `org.jasypt.spring.security.PBEPasswordEncoder` class with the `org.jasypt.util.text.BasicTextEncryptor` class, which provides similar functionality for encrypting and checking passwords. Note that the `BasicTextEncryptor` class does not have a direct equivalent to the `PBEPasswordEncoder` class's `setAlgorithm` method, so you will need to set the encryption algorithm in a different way, such as by using a system property or configuration file. Also note that the `matches` method in this patch uses the `checkPassword` method instead of the `matches` method, which has a slightly different signature but achieves the same purpose.