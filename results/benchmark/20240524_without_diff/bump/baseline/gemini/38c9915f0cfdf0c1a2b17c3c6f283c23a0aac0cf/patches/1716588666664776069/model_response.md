```java
  import org.cactoos.time.ZonedDateTimeOf;

  import java.time.ZoneId;
  import java.time.ZonedDateTime;

  public class RtTransaction {

      private final ZonedDateTime creationDate;

      public RtTransaction(final String creationDate) {
          this.creationDate = ZonedDateTimeOf.of(creationDate, ZoneId.of("UTC"));
      }

      public ZonedDateTime getCreationDate() {
          return creationDate;
      }

  }
```