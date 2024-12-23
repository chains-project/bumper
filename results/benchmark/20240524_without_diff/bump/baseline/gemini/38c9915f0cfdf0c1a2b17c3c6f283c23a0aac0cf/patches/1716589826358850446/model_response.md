```java
  import org.cactoos.list.ListOf;
  import io.zold.api.RtTransaction;
  import io.zold.api.RtTransactionBuilder;
  import io.zold.api.ZoldException;
  import java.util.ArrayList;
  import java.util.List;

  public class RtTransaction {

    private final String id;
    private final String sender;
    private final String recipient;
    private final Long amount;
    private final Long fee;
    private final Long timestamp;
    private final String signature;
    private final String hash;
    private final List<RtTransaction> references;

    public RtTransaction(String id, String sender, String recipient, Long amount, Long fee, Long timestamp, String signature, String hash, List<RtTransaction> references) {
      this.id = id;
      this.sender = sender;
      this.recipient = recipient;
      this.amount = amount;
      this.fee = fee;
      this.timestamp = timestamp;
      this.signature = signature;
      this.hash = hash;
      this.references = references;
    }

    public String getId() {
      return id;
    }

    public String getSender() {
      return sender;
    }

    public String getRecipient() {
      return recipient;
    }

    public Long getAmount() {
      return amount;
    }

    public Long getFee() {
      return fee;
    }

    public Long getTimestamp() {
      return timestamp;
    }

    public String getSignature() {
      return signature;
    }

    public String getHash() {
      return hash;
    }

    public List<RtTransaction> getReferences() {
      return references;
    }

    public static RtTransactionBuilder builder() {
      return new RtTransactionBuilder();
    }

    public static class RtTransactionBuilder {

      private String id;
      private String sender;
      private String recipient;
      private Long amount;
      private Long fee;
      private Long timestamp;
      private String signature;
      private String hash;
      private List<RtTransaction> references = new ArrayList<>();

      public RtTransactionBuilder() {
      }

      public RtTransactionBuilder id(String id) {
        this.id = id;
        return this;
      }

      public RtTransactionBuilder sender(String sender) {
        this.sender = sender;
        return this;
      }

      public RtTransactionBuilder recipient(String recipient) {
        this.recipient = recipient;
        return this;
      }

      public RtTransactionBuilder amount(Long amount) {
        this.amount = amount;
        return this;
      }

      public RtTransactionBuilder fee(Long fee) {
        this.fee = fee;
        return this;
      }

      public RtTransactionBuilder timestamp(Long timestamp) {
        this.timestamp = timestamp;
        return this;
      }

      public RtTransactionBuilder signature(String signature) {
        this.signature = signature;
        return this;
      }

      public RtTransactionBuilder hash(String hash) {
        this.hash = hash;
        return this;
      }

      public RtTransactionBuilder references(List<RtTransaction> references) {
        this.references = references;
        return this;
      }

      public RtTransaction build() {
        if (id == null) {
          throw new ZoldException("Id is required");
        }
        if (sender == null) {
          throw new ZoldException("Sender is required");
        }
        if (recipient == null) {
          throw new ZoldException("Recipient is required");
        }
        if (amount == null) {
          throw new ZoldException("Amount is required");
        }
        if (fee == null) {
          throw new ZoldException("Fee is required");
        }
        if (timestamp == null) {
          throw new ZoldException("Timestamp is required");
        }
        if (signature == null) {
          throw new ZoldException("Signature is required");
        }
        if (hash == null) {
          throw new ZoldException("Hash is required");
        }
        return new RtTransaction(id, sender, recipient, amount, fee, timestamp, signature, hash, references);
      }
    }
  }
```