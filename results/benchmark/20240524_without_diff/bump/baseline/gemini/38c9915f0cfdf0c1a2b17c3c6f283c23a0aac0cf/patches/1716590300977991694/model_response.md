```java
import org.cactoos.scalar.StickyScalar;

public class RtTransaction {

    private final StickyScalar<String> id;

    public RtTransaction(String id) {
        this.id = new StickyScalar<>(id);
    }

    public String getId() {
        return id.value();
    }
}
```