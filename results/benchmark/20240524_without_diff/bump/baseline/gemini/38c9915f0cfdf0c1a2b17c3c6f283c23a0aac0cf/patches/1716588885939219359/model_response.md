```java
import org.cactoos.text.FormattedText;
import org.cactoos.text.TextOf;

public class RtTransaction {

    public String transactionId(String transactionId) {
        return new FormattedText("Transaction ID: %s", new TextOf(transactionId)).asString();
    }
}
```