```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder extends StandardPBEStringEncryptor {

    public GeoStorePBEPasswordEncoder() {
        super();
        setAlgorithm("PBEWithMD5AndDES");
        setKeyObtentionIterations(1000);
        setPoolSize(1);
        setProviderName("SunJCE");
        setSaltGeneratorClassName("org.jasypt.salt.RandomSaltGenerator");
        setStringOutputType("base64");
    }
}
```