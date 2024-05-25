```java
import org.cactoos.scalar.UncheckedScalar;

import java.util.Map;

public class RtTransaction {

    public static final String TRANSACTION_ID = "transactionId";
    public static final String TRANSACTION_TYPE = "transactionType";
    public static final String TRANSACTION_STATUS = "transactionStatus";
    public static final String TRANSACTION_AMOUNT = "transactionAmount";
    public static final String TRANSACTION_CURRENCY = "transactionCurrency";
    public static final String TRANSACTION_FEE = "transactionFee";
    public static final String TRANSACTION_DATE = "transactionDate";
    public static final String TRANSACTION_DETAILS = "transactionDetails";

    private final Map<String, Object> data;

    public RtTransaction(Map<String, Object> data) {
        this.data = data;
    }

    public String getTransactionId() {
        return (String) data.get(TRANSACTION_ID);
    }

    public String getTransactionType() {
        return (String) data.get(TRANSACTION_TYPE);
    }

    public String getTransactionStatus() {
        return (String) data.get(TRANSACTION_STATUS);
    }

    public double getTransactionAmount() {
        return (double) data.get(TRANSACTION_AMOUNT);
    }

    public String getTransactionCurrency() {
        return (String) data.get(TRANSACTION_CURRENCY);
    }

    public double getTransactionFee() {
        return (double) data.get(TRANSACTION_FEE);
    }

    public String getTransactionDate() {
        return (String) data.get(TRANSACTION_DATE);
    }

    public Map<String, Object> getTransactionDetails() {
        return (Map<String, Object>) data.get(TRANSACTION_DETAILS);
    }
}
```