```java
import org.cactoos.scalar.IoCheckedScalar;

import java.io.IOException;

public class RtTransaction {

    public static IoCheckedScalar<String> buildTransaction(String transactionId, String transactionType, String transactionData) {
        return new IoCheckedScalar<>(() -> {
            // Build the transaction string
            StringBuilder transaction = new StringBuilder();
            transaction.append("Transaction ID: ").append(transactionId).append("\n");
            transaction.append("Transaction Type: ").append(transactionType).append("\n");
            transaction.append("Transaction Data: ").append(transactionData).append("\n");

            // Return the transaction string
            return transaction.toString();
        });
    }
}
```