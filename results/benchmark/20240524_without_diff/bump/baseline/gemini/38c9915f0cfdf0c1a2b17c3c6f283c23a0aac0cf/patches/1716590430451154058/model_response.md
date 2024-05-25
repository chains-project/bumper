```java
  import org.cactoos.scalar.StickyScalar;
  import io.zold.api.RtTransaction;
  import io.zold.api.RtTransaction.RtTransactionBuilder;

  public class RtTransaction {

      private final StickyScalar<String> id;
      private final StickyScalar<String> hash;
      private final StickyScalar<String> sender;
      private final StickyScalar<String> recipient;
      private final StickyScalar<String> amount;
      private final StickyScalar<String> fee;
      private final StickyScalar<String> timestamp;
      private final StickyScalar<String> confirmations;
      private final StickyScalar<String> type;
      private final StickyScalar<String> height;
      private final StickyScalar<String> block;
      private final StickyScalar<String> signature;
      private final StickyScalar<String> payload;
      private final StickyScalar<String> payloadHash;

      public RtTransaction(RtTransactionBuilder builder) {
          this.id = builder.id();
          this.hash = builder.hash();
          this.sender = builder.sender();
          this.recipient = builder.recipient();
          this.amount = builder.amount();
          this.fee = builder.fee();
          this.timestamp = builder.timestamp();
          this.confirmations = builder.confirmations();
          this.type = builder.type();
          this.height = builder.height();
          this.block = builder.block();
          this.signature = builder.signature();
          this.payload = builder.payload();
          this.payloadHash = builder.payloadHash();
      }

      public String id() {
          return this.id.value();
      }

      public String hash() {
          return this.hash.value();
      }

      public String sender() {
          return this.sender.value();
      }

      public String recipient() {
          return this.recipient.value();
      }

      public String amount() {
          return this.amount.value();
      }

      public String fee() {
          return this.fee.value();
      }

      public String timestamp() {
          return this.timestamp.value();
      }

      public String confirmations() {
          return this.confirmations.value();
      }

      public String type() {
          return this.type.value();
      }

      public String height() {
          return this.height.value();
      }

      public String block() {
          return this.block.value();
      }

      public String signature() {
          return this.signature.value();
      }

      public String payload() {
          return this.payload.value();
      }

      public String payloadHash() {
          return this.payloadHash.value();
      }

      public static RtTransactionBuilder builder() {
          return new RtTransactionBuilder();
      }

      public static class RtTransactionBuilder {

          private StickyScalar<String> id;
          private StickyScalar<String> hash;
          private StickyScalar<String> sender;
          private StickyScalar<String> recipient;
          private StickyScalar<String> amount;
          private StickyScalar<String> fee;
          private StickyScalar<String> timestamp;
          private StickyScalar<String> confirmations;
          private StickyScalar<String> type;
          private StickyScalar<String> height;
          private StickyScalar<String> block;
          private StickyScalar<String> signature;
          private StickyScalar<String> payload;
          private StickyScalar<String> payloadHash;

          public RtTransactionBuilder id(String id) {
              this.id = new StickyScalar<>(id);
              return this;
          }

          public RtTransactionBuilder hash(String hash) {
              this.hash = new StickyScalar<>(hash);
              return this;
          }

          public RtTransactionBuilder sender(String sender) {
              this.sender = new StickyScalar<>(sender);
              return this;
          }

          public RtTransactionBuilder recipient(String recipient) {
              this.recipient = new StickyScalar<>(recipient);
              return this;
          }

          public RtTransactionBuilder amount(String amount) {
              this.amount = new StickyScalar<>(amount);
              return this;
          }

          public RtTransactionBuilder fee(String fee) {
              this.fee = new StickyScalar<>(fee);
              return this;
          }

          public RtTransactionBuilder timestamp(String timestamp) {
              this.timestamp = new StickyScalar<>(timestamp);
              return this;
          }

          public RtTransactionBuilder confirmations(String confirmations) {
              this.confirmations = new StickyScalar<>(confirmations);
              return this;
          }

          public RtTransactionBuilder type(String type) {
              this.type = new StickyScalar<>(type);
              return this;
          }

          public RtTransactionBuilder height(String height) {
              this.height = new StickyScalar<>(height);
              return this;
          }

          public RtTransactionBuilder block(String block) {
              this.block = new StickyScalar<>(block);
              return this;
          }

          public RtTransactionBuilder signature(String signature) {
              this.signature = new StickyScalar<>(signature);
              return this;
          }

          public RtTransactionBuilder payload(String payload) {
              this.payload = new StickyScalar<>(payload);
              return this;
          }

          public RtTransactionBuilder payloadHash(String payloadHash) {
              this.payloadHash = new StickyScalar<>(payloadHash);
              return this;
          }

          public RtTransaction build() {
              return new RtTransaction(this);
          }
      }
  }
```