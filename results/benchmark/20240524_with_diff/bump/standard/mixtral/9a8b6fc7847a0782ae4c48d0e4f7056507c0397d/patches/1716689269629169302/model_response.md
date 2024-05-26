Here is the updated code for the `GeoStorePBEPasswordEncoder` class that uses the new `org.jasypt.spring.security.PasswordEncoder` instead of the removed `org.jasypt.spring.security.PBEPasswordEncoder`:
```java
import org.jasypt.spring.security.PasswordEncoder;
import org.jasypt.util.password.BasicPasswordEncryptor;

public class GeoStorePBEPasswordEncoder {

    private PasswordEncoder passwordEncoder;

    public GeoGeoStorePBEPasswordEncoder() {
        BasicPasswordEncryptor passwordEncryptor = new BasicPasswordEncryptor();
        this.passwordEncoder = new PasswordEncoder() {
            @Override
            public String encodePassword(String rawPassword, Object salt) {
                return passwordEncryptor.encryptPassword(rawPassword);
            }

            @Override
::$
```