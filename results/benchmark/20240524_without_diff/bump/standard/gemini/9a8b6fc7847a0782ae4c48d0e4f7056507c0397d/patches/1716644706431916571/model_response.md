```java
import org.jasypt.encryption.pbe.StandardPBEPasswordEncoder;

public class GeoStorePBEPasswordEncoder extends StandardPBEPasswordEncoder {

    public GeoStorePBEPasswordEncoder(String password) {
        super(password);
    }
}
```