```java
import java.time.ZonedDateTime;

import org.cactoos.time.ZonedDateTimeOf;

public class RtTransaction {

    // ...

    public ZonedDateTime getCreatedAt() {
        return new ZonedDateTimeOf(createdAt).value();
    }

    // ...
}
```