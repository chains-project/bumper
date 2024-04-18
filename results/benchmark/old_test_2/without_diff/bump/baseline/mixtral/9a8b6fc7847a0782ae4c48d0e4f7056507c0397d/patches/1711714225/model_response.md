Here is a possible patch for the failing code:

```java
import org.jasypt.util.text.BasicTextEncryptor;

@Component
public class GeoStorePBEPasswordEncoder {

    @Value("${geostore.security.password.encoder.salt}")
    private String salt;

    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    @PostConstruct
    public void init() {
        encryptor.setAlgorithm("PBEWithMD5AndTripleDES");
        encryptor.setPassword(salt);
    }

    @Override
    public String encode(String rawPass) {
        return encryptor.encrypt(rawPass);
    }

    @Override
    public boolean matches(String encPass, String rawPass) {
        return encryptor.checkPassword(rawPass, encPass);
    }
}
```

In this patch, we replace the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package with the `BasicTextEncryptor` class from the `org.jasypt.util.text` package. We also set the algorithm and password for the encryptor in the `init` method.

Note that this patch assumes that the `geostore.security.password.encoder.salt` property is defined in the application's configuration. If this property is not defined, the `init` method will throw a `NullPointerException`.

Also note that this patch uses the `PBEWithMD5AndTripleDES` algorithm, which is not recommended for new applications due to its weaknesses. If possible, it is recommended to use a stronger algorithm such as `PBKDF2WithHmacSHA512`.