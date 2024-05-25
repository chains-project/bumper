```java
import com.google.common.base.Strings;
import org.cactoos.text.TextOf;

import java.util.Optional;

public class RtTransaction {
    public String getRtTransactionId() {
        String rtTransactionId = this.getRtTransactionId();
        if (Strings.isNullOrEmpty(rtTransactionId)) {
            return Optional.ofNullable(this.getRtTransactionId()).orElse("");
        }
        return rtTransactionId;
    }

    public String getRtTransactionId() {
        return new TextOf(this.getRtTransactionId()).asString();
    }
}
```