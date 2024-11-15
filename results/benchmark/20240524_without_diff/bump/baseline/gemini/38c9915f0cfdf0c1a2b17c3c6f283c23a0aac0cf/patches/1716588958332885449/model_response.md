```java
  import org.cactoos.text.FormattedText;

  import java.time.Instant;
  import java.util.Optional;

  public class RtTransaction {

    private final String id;
    private final String hash;
    private final String blockHash;
    private final Instant timestamp;
    private final Optional<String> from;
    private final Optional<String> to;
    private final String value;
    private final String gasPrice;
    private final String gas;
    private final String input;
    private final String nonce;
    private final String confirmations;

    public RtTransaction(String id, String hash, String blockHash, Instant timestamp, Optional<String> from, Optional<String> to, String value, String gasPrice, String gas, String input, String nonce, String confirmations) {
      this.id = id;
      this.hash = hash;
      this.blockHash = blockHash;
      this.timestamp = timestamp;
      this.from = from;
      this.to = to;
      this.value = value;
      this.gasPrice = gasPrice;
      this.gas = gas;
      this.input = input;
      this.nonce = nonce;
      this.confirmations = confirmations;
    }

    public String getId() {
      return id;
    }

    public String getHash() {
      return hash;
    }

    public String getBlockHash() {
      return blockHash;
    }

    public Instant getTimestamp() {
      return timestamp;
    }

    public Optional<String> getFrom() {
      return from;
    }

    public Optional<String> getTo() {
      return to;
    }

    public String getValue() {
      return value;
    }

    public String getGasPrice() {
      return gasPrice;
    }

    public String getGas() {
      return gas;
    }

    public String getInput() {
      return input;
    }

    public String getNonce() {
      return nonce;
    }

    public String getConfirmations() {
      return confirmations;
    }

    @Override
    public String toString() {
      return new FormattedText(
          "RtTransaction(id=%s, hash=%s, blockHash=%s, timestamp=%s, from=%s, to=%s, value=%s, gasPrice=%s, gas=%s, input=%s, nonce=%s, confirmations=%s)",
          id, hash, blockHash, timestamp, from, to, value, gasPrice, gas, input, nonce, confirmations).asString();
    }
  }
```