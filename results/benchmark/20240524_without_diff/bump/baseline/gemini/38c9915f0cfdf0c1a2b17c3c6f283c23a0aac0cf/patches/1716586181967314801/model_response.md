```java
import org.cactoos.scalar.SolidScalar;

public class WalletsIn {

    public SolidScalar<String> walletsIn(String wallet, String apikey) {
        return new SolidScalar<>("{\"wallet\":\"" + wallet + "\",\"apikey\":\"" + apikey + "\"}");
    }
}
```