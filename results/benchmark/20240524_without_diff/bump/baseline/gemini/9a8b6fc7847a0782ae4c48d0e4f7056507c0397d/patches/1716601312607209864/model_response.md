```java
import org.jasypt.encryption.pbe.StandardPBEByteEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEByteEncryptor {

    private static final String ALGORITHM = "PBEWithMD5AndDES";
    private static final String SALT_SOURCE = "GeoStore";

    public GeoStorePBEPasswordEncoder() {
        setAlgorithm(ALGORITHM);
        setSaltSource(SALT_SOURCE);
    }
}
```