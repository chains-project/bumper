```java
import org.cactoos.scalar.SolidScalar;

public class WalletsIn {

    public SolidScalar<String> walletsIn(String address) {
        return new SolidScalar<>(address);
    }
}
```