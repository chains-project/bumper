```java
import org.jasypt.util.password.ConfigurablePasswordEncryptor;

public class GeoStorePBEPasswordEncoder extends ConfigurablePasswordEncryptor {

    public GeoStorePBEPasswordEncoder() {
        super();
        setAlgorithm("PBEWithMD5AndDES");
    }

}
```