```java
import org.jasypt.encryption.pbe.StandardPBEStringEncryptor;

public class GeoStorePBEPasswordEncoder {

    private StandardPBEStringEncryptor encryptor;

    public GeoStorePBEPasswordEncoder() {
        encryptor = new StandardPBEStringEncryptor();
        encryptor.setPassword("geosolutions");
        encryptor.setAlgorithm("PBEWithMD5AndDES");
    }

    public String encode(String password) {
        return encryptor.encrypt(password);
    }

    public boolean matches(String password, String encodedPassword) {
        return encryptor.checkPassword(password, encodedPassword);
    }
}
```