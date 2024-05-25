```java
  import org.cactoos.text.FormattedText;

  public class RtTransaction {

    // ... other methods

    public String getTransactionId() {
      return new FormattedText("%s-%s", this.getRtId(), this.getTransactionType()).asString();
    }

    // ... other methods

  }
```