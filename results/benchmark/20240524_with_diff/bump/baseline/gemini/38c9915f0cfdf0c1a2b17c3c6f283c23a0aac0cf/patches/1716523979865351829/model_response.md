```java
import org.cactoos.text.TextOfScalar;

public class WalletsIn {

    public CollectionEnvelope walletsIn(String key, String value) {
        return new CollectionEnvelope(new TextOfScalar(key + value));
    }
}
```