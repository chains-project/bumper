```java
  import io.zold.api.RtTransaction;
  import org.cactoos.text.FormattedText;
  import org.cactoos.text.TextOf;

  import java.math.BigDecimal;
  import java.util.List;

  public class RtTransaction {

      private final String txId;
      private final String hash;
      private final BigDecimal amount;
      private final String fee;
      private final String from;
      private final String to;
      private final String memo;
      private final String timestamp;
      private final String confirmations;
      private final String blockHash;
      private final String blockHeight;
      private final List<String> vin;
      private final List<String> vout;

      public RtTransaction(String txId, String hash, BigDecimal amount, String fee, String from, String to, String memo, String timestamp, String confirmations, String blockHash, String blockHeight, List<String> vin, List<String> vout) {
          this.txId = txId;
          this.hash = hash;
          this.amount = amount;
          this.fee = fee;
          this.from = from;
          this.to = to;
          this.memo = memo;
          this.timestamp = timestamp;
          this.confirmations = confirmations;
          this.blockHash = blockHash;
          this.blockHeight = blockHeight;
          this.vin = vin;
          this.vout = vout;
      }

      public String getTxId() {
          return txId;
      }

      public String getHash() {
          return hash;
      }

      public BigDecimal getAmount() {
          return amount;
      }

      public String getFee() {
          return fee;
      }

      public String getFrom() {
          return from;
      }

      public String getTo() {
          return to;
      }

      public String getMemo() {
          return memo;
      }

      public String getTimestamp() {
          return timestamp;
      }

      public String getConfirmations() {
          return confirmations;
      }

      public String getBlockHash() {
          return blockHash;
      }

      public String getBlockHeight() {
          return blockHeight;
      }

      public List<String> getVin() {
          return vin;
      }

      public List<String> getVout() {
          return vout;
      }

      @Override
      public String toString() {
          return new FormattedText(
                  "Transaction ID: %s\n" +
                          "Hash: %s\n" +
                          "Amount: %s\n" +
                          "Fee: %s\n" +
                          "From: %s\n" +
                          "To: %s\n" +
                          "Memo: %s\n" +
                          "Timestamp: %s\n" +
                          "Confirmations: %s\n" +
                          "Block Hash: %s\n" +
                          "Block Height: %s\n" +
                          "Vin: %s\n" +
                          "Vout: %s",
                  txId, hash, amount, fee, from, to, memo, timestamp, confirmations, blockHash, blockHeight, vin, vout
          ).asString();
      }
  }
```