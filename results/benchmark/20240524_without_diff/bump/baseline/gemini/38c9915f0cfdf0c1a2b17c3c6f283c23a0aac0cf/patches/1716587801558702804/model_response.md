```java
  import org.cactoos.scalar.UncheckedScalar;

  import io.zold.api.RtTransaction;

  public class RtTransaction {

    private final UncheckedScalar<String> txId;

    private final UncheckedScalar<String> hash;

    private final UncheckedScalar<String> blockHash;

    private final UncheckedScalar<Integer> blockNumber;

    private final UncheckedScalar<Long> blockTimestamp;

    private final UncheckedScalar<String> from;

    private final UncheckedScalar<String> to;

    private final UncheckedScalar<String> value;

    private final UncheckedScalar<String> fee;

    private final UncheckedScalar<String> gas;

    private final UncheckedScalar<String> gasPrice;

    private final UncheckedScalar<String> nonce;

    private final UncheckedScalar<String> input;

    private final UncheckedScalar<String> confirmations;

    private final UncheckedScalar<String> status;

    private final UncheckedScalar<String> error;

    public RtTransaction(UncheckedScalar<String> txId, UncheckedScalar<String> hash, UncheckedScalar<String> blockHash, UncheckedScalar<Integer> blockNumber, UncheckedScalar<Long> blockTimestamp, UncheckedScalar<String> from, UncheckedScalar<String> to, UncheckedScalar<String> value, UncheckedScalar<String> fee, UncheckedScalar<String> gas, UncheckedScalar<String> gasPrice, UncheckedScalar<String> nonce, UncheckedScalar<String> input, UncheckedScalar<String> confirmations, UncheckedScalar<String> status, UncheckedScalar<String> error) {
      this.txId = txId;
      this.hash = hash;
      this.blockHash = blockHash;
      this.blockNumber = blockNumber;
      this.blockTimestamp = blockTimestamp;
      this.from = from;
      this.to = to;
      this.value = value;
      this.fee = fee;
      this.gas = gas;
      this.gasPrice = gasPrice;
      this.nonce = nonce;
      this.input = input;
      this.confirmations = confirmations;
      this.status = status;
      this.error = error;
    }

    public String getTxId() {
      return txId.value();
    }

    public String getHash() {
      return hash.value();
    }

    public String getBlockHash() {
      return blockHash.value();
    }

    public int getBlockNumber() {
      return blockNumber.value();
    }

    public long getBlockTimestamp() {
      return blockTimestamp.value();
    }

    public String getFrom() {
      return from.value();
    }

    public String getTo() {
      return to.value();
    }

    public String getValue() {
      return value.value();
    }

    public String getFee() {
      return fee.value();
    }

    public String getGas() {
      return gas.value();
    }

    public String getGasPrice() {
      return gasPrice.value();
    }

    public String getNonce() {
      return nonce.value();
    }

    public String getInput() {
      return input.value();
    }

    public String getConfirmations() {
      return confirmations.value();
    }

    public String getStatus() {
      return status.value();
    }

    public String getError() {
      return error.value();
    }
  }
```