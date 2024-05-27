```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {

    public GeoStorePBEPasswordEncoder() {
        super();
        setAlgorithm("PBEWithMD5AndDES");
        setPassword("password");
    }
}
```