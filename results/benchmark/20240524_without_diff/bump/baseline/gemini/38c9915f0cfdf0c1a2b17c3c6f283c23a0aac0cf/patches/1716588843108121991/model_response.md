```java
import org.cactoos.text.FormattedText;
import org.cactoos.text.TextOf;

public class RtTransaction {
    public String getRtTransactionText(String rtTransactionId) {
        String rtTransactionText = new FormattedText(
                "RT Transaction: %s",
                new TextOf(rtTransactionId)
        ).asString();
        return rtTransactionText;
    }
}
```