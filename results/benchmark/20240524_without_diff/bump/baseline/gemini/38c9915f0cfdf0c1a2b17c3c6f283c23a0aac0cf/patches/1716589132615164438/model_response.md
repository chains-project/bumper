```java
import org.cactoos.text.TrimmedText;

  public String getRtTransactionId(String rtTransactionId) {
    return new TrimmedText(rtTransactionId).asString();
  }
```