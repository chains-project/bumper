```java
import org.cactoos.text.TextOf;

public class RtTransaction {

    public String getRtTransactionId() {
        return new TextOf(this).asString();
    }
}
```