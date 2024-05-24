```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.text.TextEncryptor;

public class GeoStoreDigestPasswordEncoder {
    public GeoStoreDigestPasswordEncoder() {
        TextEncryptor encryptor = new StandardPBEStringEncryptor();
        encryptor.initialize();
    }
}
```