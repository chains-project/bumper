```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {

    public GeoStorePBEPasswordEncoder() {
        super();
        setPassword("geosolutions");
        setAlgorithm("PBEWithMD5AndDES");
    }
}
```