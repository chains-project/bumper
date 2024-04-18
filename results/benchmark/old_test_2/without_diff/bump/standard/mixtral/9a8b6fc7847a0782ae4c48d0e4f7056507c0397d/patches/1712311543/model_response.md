Here's the proposed patch:
```java
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {
    private BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();

    public String encode(String rawPass) {
        return passwordEncryptor.encryptPassword(rawPass);
    }

    public boolean matches(String rawPass, String encPass) {
        return passwordEncryptor.checkPassword(rawPass, encPass);
    }
}
```
In this patch, I replaced the `PBEPasswordEncoder` class from the `org.jasypt.spring.security` package with the `BasicPasswordEncryptor` class from the `org.jasypt.util.password` package, which should provide similar functionality. I also updated the method calls in the `encode` and `matches` methods to use the new class.