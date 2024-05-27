Here is the proposed patch:

```java
import org.jasypt.util.text.BasicTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    private BasicTextEncryptor encryptor = new BasicTextEncryptor();

    // ... other methods ...

    public String encode(String rawPass) {
        encryptor.setPassword("your-secret-key-here");
        return encryptor.encrypt(rawPass);
    }

    public boolean matches(String rawPass, String encodedPass) {
        encryptor.setPassword("your-secret-key-here");
        return encryptor.checkPassword(rawPass, encodedPass);
    }
}
```

Note that this patch replaces the `PBEPasswordEncoder` with `BasicTextEncryptor` from the `org.jasypt.util.text` package. The `encode` and `matches` methods have been updated accordingly. Also, note that you need to replace `"your-secret-key-here"` with your own secret key.