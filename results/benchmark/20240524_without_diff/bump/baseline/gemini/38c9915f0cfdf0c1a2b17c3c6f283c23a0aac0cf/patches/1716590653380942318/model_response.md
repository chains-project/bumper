```java
import org.cactoos.text.TextOf;

public class RtTransaction {
    public String getTransactionId() {
        return new TextOf(this.toString()).asString();
    }
}
```