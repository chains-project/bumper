```java
import org.cactoos.text.TrimmedText;

import java.util.Optional;

public class RtTransaction {

    public String getTxId() {
        Optional<String> txId = Optional.ofNullable(this.data.get("txid"));
        return txId.map(new TrimmedText()).orElse(null);
    }

    // ... other methods ...
}
```