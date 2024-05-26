```java
import org.jasypt.util.password.StrongPasswordEncryptor;

public class GeoStorePBEPasswordEncoder extends StrongPasswordEncryptor {

    public GeoStorePBEPasswordEncoder() {
        super();
    }

    public GeoStorePBEPasswordEncoder(String password) {
        super(password);
    }

}
```