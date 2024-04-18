Here's the proposed patch:
```java
import org.jasypt.util.text.StrongTextEncryptor;

public class GeoStorePBEPasswordEncoder {
    private StrongTextEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        this.encryptor = new StrongTextEncryptor();
        this.encryptor.setAlgorithm("PBEWithMD5AndTripleDES");
    }

    public String encode(String rawPass) {
        return encryptor.encrypt(rawPass);
    }

    public boolean matches(String rawPass, String encodedPass) {
        return encryptor.checkPassword(rawPass, encodedPass);
    }
}
```
Note: This patch replaces the `PBEPasswordEncoder` from the `org.jasypt.spring.security` package with the `StrongTextEncryptor` from the `org.jasypt.util.text` package. The `StrongTextEncryptor` provides similar functionality to the `PBEPasswordEncoder`. The algorithm used by the `StrongTextEncryptor` has been set to `PBEWithMD5AndTripleDES` to match the algorithm used by the `PBEPasswordEncoder`.