```java
import org.cactoos.scalar.ItemAt;

import java.util.List;

public class RtTransaction {

    public RtTransaction(String id, String hash, String blockHash, long blockHeight, long timestamp, String from, String to, String value, String fee, String gasPrice, String gasUsed, String nonce, String status, String confirmations, List<RtLog> logs) {
        this.id = id;
        this.hash = hash;
        this.blockHash = blockHash;
        this.blockHeight = blockHeight;
        this.timestamp = timestamp;
        this.from = from;
        this.to = to;
        this.value = value;
        this.fee = fee;
        this.gasPrice = gasPrice;
        this.gasUsed = gasUsed;
        this.nonce = nonce;
        this.status = status;
        this.confirmations = confirmations;
        this.logs = logs;
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

    public long getBlockHeight() {
        return blockHeight;
    }

    public long getTimestamp() {
        return timestamp;
    }

    public String getFrom() {
        return from;
    }

    public String getTo() {
        return to;
    }

    public String getValue() {
        return value;
    }

    public String getFee() {
        return fee;
    }

    public String getGasPrice() {
        return gasPrice;
    }

    public String getGasUsed() {
        return gasUsed;
    }

    public String getNonce() {
        return nonce;
    }

    public String getStatus() {
        return status;
    }

    public String getConfirmations() {
        return confirmations;
    }

    public List<RtLog> getLogs() {
        return logs;
    }

    private final String id;
    private final String hash;
    private final String blockHash;
    private final long blockHeight;
    private final long timestamp;
    private final String from;
    private final String to;
    private final String value;
    private final String fee;
    private final String gasPrice;
    private final String gasUsed;
    private final String nonce;
    private final String status;
    private final String confirmations;
    private final List<RtLog> logs;
}
```