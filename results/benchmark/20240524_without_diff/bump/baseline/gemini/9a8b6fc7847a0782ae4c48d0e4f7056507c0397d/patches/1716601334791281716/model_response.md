```java
import org.jasypt.encryption.pbe.StandardPBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends StandardPBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder() {
        super();
        // Set the algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password) {
        super(password);
        // Set the algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password, int keyObtentionIterations) {
        super(password, keyObtentionIterations);
        // Set the algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password, int keyObtentionIterations, String saltGeneratorClassName) {
        super(password, keyObtentionIterations, saltGeneratorClassName);
        // Set the algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }

    public GeoStorePBEPasswordEncoder(String password, int keyObtentionIterations, String saltGeneratorClassName, String stringOutputType) {
        super(password, keyObtentionIterations, saltGeneratorClassName, stringOutputType);
        // Set the algorithm to PBEWithMD5AndDES
        setAlgorithm("PBEWithMD5AndDES");
    }
}
```