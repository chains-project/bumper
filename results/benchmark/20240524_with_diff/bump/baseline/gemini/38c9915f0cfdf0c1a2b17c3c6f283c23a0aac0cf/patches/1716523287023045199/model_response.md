```java
import org.cactoos.iterable.Solid;
import org.cactoos.map.SolidMap;
import org.cactoos.scalar.Scalar;
import org.cactoos.scalar.Solid;

import java.util.Map;

public class WalletsIn {

    public Map<String, Scalar<String>> walletsIn(Scalar<String> address) {
        return new SolidMap<>(
                new Solid<>(
                        new SolidScalar<>(address),
                        new SolidScalar<>(address),
                        new SolidScalar<>(address),
                        new SolidScalar<>(address)
                )
        );
    }
}
```