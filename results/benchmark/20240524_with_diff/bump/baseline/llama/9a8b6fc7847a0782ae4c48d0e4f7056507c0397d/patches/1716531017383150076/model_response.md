```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStoreDigestPasswordEncoder {
    public GeoStoreDigestPasswordEncoder() {
        StrongPasswordEncryptor passwordEncryptor = new StrongPasswordEncryptor();
        passwordEncryptor.setStringOutputType("base64");
    }
}
```