```java
  import org.cactoos.scalar.UncheckedScalar;
  import io.zold.api.RtTransaction;

  public class RtTransaction {

    public RtTransaction(UncheckedScalar<Long> height, UncheckedScalar<Long> timestamp, UncheckedScalar<String> hash, UncheckedScalar<String> blockHash, UncheckedScalar<String> fromAddress, UncheckedScalar<String> toAddress, UncheckedScalar<Long> amount, UncheckedScalar<String> assetId) {
      this.height = height;
      this.timestamp = timestamp;
      this.hash = hash;
      this.blockHash = blockHash;
      this.fromAddress = fromAddress;
      this.toAddress = toAddress;
      this.amount = amount;
      this.assetId = assetId;
    }

    private final UncheckedScalar<Long> height;
    private final UncheckedScalar<Long> timestamp;
    private final UncheckedScalar<String> hash;
    private final UncheckedScalar<String> blockHash;
    private final UncheckedScalar<String> fromAddress;
    private final UncheckedScalar<String> toAddress;
    private final UncheckedScalar<Long> amount;
    private final UncheckedScalar<String> assetId;

    public UncheckedScalar<Long> getHeight() {
      return height;
    }

    public UncheckedScalar<Long> getTimestamp() {
      return timestamp;
    }

    public UncheckedScalar<String> getHash() {
      return hash;
    }

    public UncheckedScalar<String> getBlockHash() {
      return blockHash;
    }

    public UncheckedScalar<String> getFromAddress() {
      return fromAddress;
    }

    public UncheckedScalar<String> getToAddress() {
      return toAddress;
    }

    public UncheckedScalar<Long> getAmount() {
      return amount;
    }

    public UncheckedScalar<String> getAssetId() {
      return assetId;
    }
  }
```