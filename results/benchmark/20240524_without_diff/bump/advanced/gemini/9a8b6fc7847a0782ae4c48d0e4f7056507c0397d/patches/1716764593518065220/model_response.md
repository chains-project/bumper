```java
import org.jasypt.encryption.pbe.StandardPBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends StandardPBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
        // Set the default algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password) {
        super(password);
        // Set the default algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password, String salt) {
        super(password, salt);
        // Set the default algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password, String salt, int keyObtentionIterations) {
        super(password, salt, keyObtentionIterations);
        // Set the default algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password, String salt, int keyObtentionIterations, String algorithm) {
        super(password, salt, keyObtentionIterations, algorithm);
    }
}
```