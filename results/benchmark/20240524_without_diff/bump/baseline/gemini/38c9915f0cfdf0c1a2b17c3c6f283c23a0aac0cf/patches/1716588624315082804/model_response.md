```java
import org.cactoos.time.ZonedDateTimeOf;

public class RtTransaction {

    private final String transactionId;
    private final String sender;
    private final String receiver;
    private final Long amount;
    private final Long fee;
    private final ZonedDateTimeOf timestamp;
    private final String status;
    private final String error;

    public RtTransaction(String transactionId, String sender, String receiver, Long amount, Long fee, ZonedDateTimeOf timestamp, String status, String error) {
        this.transactionId = transactionId;
        this.sender = sender;
        this.receiver = receiver;
        this.amount = amount;
        this.fee = fee;
        this.timestamp = timestamp;
        this.status = status;
        this.error = error;
    }

    public String getTransactionId() {
        return transactionId;
    }

    public String getSender() {
        return sender;
    }

    public String getReceiver() {
        return receiver;
    }

    public Long getAmount() {
        return amount;
    }

    public Long getFee() {
        return fee;
    }

    public ZonedDateTimeOf getTimestamp() {
        return timestamp;
    }

    public String getStatus() {
        return status;
    }

    public String getError() {
        return error;
    }
}
```