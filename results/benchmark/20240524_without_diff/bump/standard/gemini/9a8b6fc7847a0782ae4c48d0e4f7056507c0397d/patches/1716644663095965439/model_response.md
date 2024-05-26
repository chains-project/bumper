```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder extends StrongPasswordEncryptor {

    public GeoStorePBEPasswordEncoder() {
        super();
    }

    public GeoStorePBEPasswordEncoder(String algorithm, int keyObtentionIterations, int saltSizeBytes, String digest) {
        super(algorithm, keyObtentionIterations, saltSizeBytes, digest);
    }
}
```