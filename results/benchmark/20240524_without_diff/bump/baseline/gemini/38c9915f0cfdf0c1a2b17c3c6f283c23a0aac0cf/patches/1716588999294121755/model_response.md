```java
import org.cactoos.text.FormattedText;
import org.cactoos.text.UncheckedText;

import java.util.function.Function;

public class RtTransaction {

    public RtTransaction(String transactionId, Function<String, String> getRtUrl) {
        this.transactionId = transactionId;
        this.getRtUrl = getRtUrl;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public String getRtUrl() {
        return getRtUrl.apply(transactionId);
    }

    public String getRtUrl(String transactionId) {
        return new UncheckedText(
                new FormattedText(
                        "https://rt.zold.io/Ticket/Display.html?id=%s",
                        transactionId
                )
        ).asString();
    }

    private final String transactionId;
    private final Function<String, String> getRtUrl;
}
```