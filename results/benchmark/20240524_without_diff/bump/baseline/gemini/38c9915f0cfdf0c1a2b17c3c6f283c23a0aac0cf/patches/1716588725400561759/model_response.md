```java
import org.cactoos.time.ZonedDateTimeOf;
import java.time.ZonedDateTime;

public class RtTransaction {

    private ZonedDateTime timestamp;

    public RtTransaction(ZonedDateTime timestamp) {
        this.timestamp = timestamp;
    }

    public ZonedDateTime getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(ZonedDateTime timestamp) {
        this.timestamp = timestamp;
    }
}
```