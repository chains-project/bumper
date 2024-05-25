```java
import org.cactoos.time.ZonedDateTimeOf;
import java.time.ZonedDateTime;

public class RtTransaction {

    public ZonedDateTime getTimestamp() {
        // return new ZonedDateTimeOf(System.currentTimeMillis()).value();
        return ZonedDateTime.now();
    }

    // ...
}
```