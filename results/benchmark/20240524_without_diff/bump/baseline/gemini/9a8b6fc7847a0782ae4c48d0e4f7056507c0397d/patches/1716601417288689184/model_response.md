```java
import org.jasypt.encryption.pbe.StandardPBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends StandardPBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
        // Set the algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }
}
```