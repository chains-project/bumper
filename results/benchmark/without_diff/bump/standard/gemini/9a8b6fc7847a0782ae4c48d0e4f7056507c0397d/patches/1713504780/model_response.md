```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;
import org.jasypt.encryption.pbe.config.EnvironmentPBEConfig;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {
    public GeoStorePBEPasswordEncoder(String password) {
        super();
        EnvironmentPBEConfig config = new EnvironmentPBEConfig();
        config.setAlgorithm("PBEWithMD5AndDES");
        config.setPassword(password);
        setConfig(config);
    }
}
```