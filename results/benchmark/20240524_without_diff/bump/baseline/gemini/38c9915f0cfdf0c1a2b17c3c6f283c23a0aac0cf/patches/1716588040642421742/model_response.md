```java
import org.cactoos.scalar.ItemAt;
import org.cactoos.scalar.LengthOf;
import org.cactoos.scalar.Scalar;

import java.util.List;

public class RtTransaction {

    public Scalar<String> getTransactionId(List<String> transactionIds) {
        return new ItemAt<>(new LengthOf<>(transactionIds), transactionIds);
    }
}
```