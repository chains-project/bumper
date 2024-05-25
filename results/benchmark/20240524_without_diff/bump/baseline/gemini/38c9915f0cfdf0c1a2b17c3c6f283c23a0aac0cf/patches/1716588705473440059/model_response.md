```java
import org.cactoos.time.ZonedDateTimeOf;

public class RtTransaction {

    public static ZonedDateTimeOf getCreatedDate(String createdDate) {
        String[] dateParts = createdDate.split("T");
        String date = dateParts[0];
        String time = dateParts[1].substring(0, 8);
        return new ZonedDateTimeOf(date + " " + time);
    }
}
```