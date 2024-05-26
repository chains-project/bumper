```java
import org.jasypt.encryption.pbe.PBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends PBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
        setAlgorithm("PBEWithMD5AndDES");
        setKey("geostore");
    }
}
```