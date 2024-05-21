```java
import org.jasypt.encryption.pbe.StandardPBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends StandardPBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
        setAlgorithm("PBEWithMD5AndDES");
    }
}
```