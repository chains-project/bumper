```java
  import org.cactoos.list.ListOf;
  import java.util.List;
  import java.util.ArrayList;
  import java.util.Arrays;

  public class RtTransaction {

    public RtTransaction(String transactionId, String from, String to, String amount, String fee, String timestamp, String hash, String blockNumber, String confirmations, String status, String type, String memo, String data, String extra, String internalTransactions) {
      this.transactionId = transactionId;
      this.from = from;
      this.to = to;
      this.amount = amount;
      this.fee = fee;
      this.timestamp = timestamp;
      this.hash = hash;
      this.blockNumber = blockNumber;
      this.confirmations = confirmations;
      this.status = status;
      this.type = type;
      this.memo = memo;
      this.data = data;
      this.extra = extra;
      this.internalTransactions = internalTransactions;
    }

    public String getTransactionId() {
      return transactionId;
    }

    public String getFrom() {
      return from;
    }

    public String getTo() {
      return to;
    }

    public String getAmount() {
      return amount;
    }

    public String getFee() {
      return fee;
    }

    public String getTimestamp() {
      return timestamp;
    }

    public String getHash() {
      return hash;
    }

    public String getBlockNumber() {
      return blockNumber;
    }

    public String getConfirmations() {
      return confirmations;
    }

    public String getStatus() {
      return status;
    }

    public String getType() {
      return type;
    }

    public String getMemo() {
      return memo;
    }

    public String getData() {
      return data;
    }

    public String getExtra() {
      return extra;
    }

    public String getInternalTransactions() {
      return internalTransactions;
    }

    private final String transactionId;
    private final String from;
    private final String to;
    private final String amount;
    private final String fee;
    private final String timestamp;
    private final String hash;
    private final String blockNumber;
    private final String confirmations;
    private final String status;
    private final String type;
    private final String memo;
    private final String data;
    private final String extra;
    private final String internalTransactions;
  }
```