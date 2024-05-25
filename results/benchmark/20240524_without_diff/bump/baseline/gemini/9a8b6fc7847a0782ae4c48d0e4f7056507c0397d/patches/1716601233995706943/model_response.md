```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder extends StrongPasswordEncryptor {

    public GeoStorePBEPasswordEncoder() {
        super();
    }

    public GeoStorePBEPasswordEncoder(String password) {
        super(password);
    }

    public GeoStorePBEPasswordEncoder(String password, int keyObtentionIterations) {
        super(password, keyObtentionIterations);
    }

    public GeoStorePBEPasswordEncoder(String password, int keyObtentionIterations, String algorithm) {
        super(password, keyObtentionIterations, algorithm);
    }

    public GeoStorePBEPasswordEncoder(String password, int keyObtentionIterations, String algorithm, String saltGeneratorClassName) {
        super(password, keyObtentionIterations, algorithm, saltGeneratorClassName);
    }
}
```