Here's the patch that you can apply to fix the error:
```java
import org.jasypt.util.text.BasicTextEncryptor;

// Change the class level import if needed
// import it.geosolutions.geostore.core.security.password.GeoStorePBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder {

    private BasicTextEncryptor textEncryptor;

    public GeoStorePBEPasswordEncoder() {
        this.textEncryptor = new BasicTextEncryptor();
        this.textEncryptor.setPassword("thisIsASecretKey");
    }

    public String encode(String rawPass) {
        return textEncryptor.encrypt(rawPass);
    }

    public boolean matches(String encPass, String rawPass) {
        return encPass.equals(textEncryptor.encrypt(rawPass));
    }
}
```
In this patch, I replaced the `PBEPasswordEncoder` class from `org.jasypt.spring.security` package with the `BasicTextEncryptor` class from `org.jasypt.util.text` package, as the former is no longer available in the newer version of the library. The `BasicTextEncryptor` class provides similar functionality, so it can be used as a drop-in replacement.

Note: You may need to adjust the encryption key and the package name of the `GeoStorePBEPasswordEncoder` class based on your specific use case.