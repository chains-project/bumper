```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {

    public GeoStorePBEPasswordEncoder(String password) {
        super();
        setPassword(password);
    }
}
```