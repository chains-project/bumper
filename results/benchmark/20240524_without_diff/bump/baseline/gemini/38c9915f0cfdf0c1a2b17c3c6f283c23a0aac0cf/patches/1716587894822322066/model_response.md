```java
package io.zold.api;

import static org.cactoos.scalar.UncheckedScalar.of;

import org.cactoos.text.FormattedText;
import org.cactoos.text.TextOf;

public class RtTransaction {

    private final String txId;

    public RtTransaction(String txId) {
        this.txId = txId;
    }

    public RtTransaction(UncheckedScalar<String> txId) {
        this(txId.value());
    }

    public String getTxId() {
        return txId;
    }

    @Override
    public String toString() {
        return new FormattedText("RtTransaction(txId=%s)", new TextOf(txId)).asString();
    }
}
```