```java
import it.geosolutions.geostore.core.security.password.GeoStorePBEPasswordEncoder;

public class PasswordEncoder {

    public static void main(String[] args) {
        GeoStorePBEPasswordEncoder encoder = new GeoStorePBEPasswordEncoder();
        String encodedPassword = encoder.encode("password");
        System.out.println("Encoded password: " + encodedPassword);
    }
}
```