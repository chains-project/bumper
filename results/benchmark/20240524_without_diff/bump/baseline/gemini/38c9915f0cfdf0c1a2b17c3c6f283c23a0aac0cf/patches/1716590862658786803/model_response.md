```java
  import org.cactoos.scalar.IoCheckedScalar;
  import static org.cactoos.text.FormattedText.textOf;

  /**
   * A transaction.
   */
  public interface RtTransaction extends Transaction {

      /**
       * The transaction's description.
       *
       * @return The description
       */
      default IoCheckedScalar<String> description() {
          return new IoCheckedScalar<>(this::getDescription);
      }

      /**
       * The transaction's description.
       *
       * @return The description
       */
      String getDescription();

      /**
       * The transaction's id.
       *
       * @return The id
       */
      default IoCheckedScalar<String> id() {
          return new IoCheckedScalar<>(this::getId);
      }

      /**
       * The transaction's id.
       *
       * @return The id
       */
      String getId();

      /**
       * The transaction's status.
       *
       * @return The status
       */
      default IoCheckedScalar<String> status() {
          return new IoCheckedScalar<>(this::getStatus);
      }

      /**
       * The transaction's status.
       *
       * @return The status
       */
      String getStatus();

      /**
       * The transaction's type.
       *
       * @return The type
       */
      default IoCheckedScalar<String> type() {
          return new IoCheckedScalar<>(this::getType);
      }

      /**
       * The transaction's type.
       *
       * @return The type
       */
      String getType();

      /**
       * The transaction's timestamp.
       *
       * @return The timestamp
       */
      default IoCheckedScalar<Long> timestamp() {
          return new IoCheckedScalar<>(this::getTimestamp);
      }

      /**
       * The transaction's timestamp.
       *
       * @return The timestamp
       */
      long getTimestamp();

      /**
       * The transaction's metadata.
       *
       * @return The metadata
       */
      default IoCheckedScalar<String> metadata() {
          return new IoCheckedScalar<>(this::getMetadata);
      }

      /**
       * The transaction's metadata.
       *
       * @return The metadata
       */
      String getMetadata();

      /**
       * The transaction's amount.
       *
       * @return The amount
       */
      default IoCheckedScalar<Long> amount() {
          return new IoCheckedScalar<>(this::getAmount);
      }

      /**
       * The transaction's amount.
       *
       * @return The amount
       */
      long getAmount();

      /**
       * The transaction's fee.
       *
       * @return The fee
       */
      default IoCheckedScalar<Long> fee() {
          return new IoCheckedScalar<>(this::getFee);
      }

      /**
       * The transaction's fee.
       *
       * @return The fee
       */
      long getFee();

      /**
       * The transaction's sender.
       *
       * @return The sender
       */
      default IoCheckedScalar<String> sender() {
          return new IoCheckedScalar<>(this::getSender);
      }

      /**
       * The transaction's sender.
       *
       * @return The sender
       */
      String getSender();

      /**
       * The transaction's recipient.
       *
       * @return The recipient
       */
      default IoCheckedScalar<String> recipient() {
          return new IoCheckedScalar<>(this::getRecipient);
      }

      /**
       * The transaction's recipient.
       *
       * @return The recipient
       */
      String getRecipient();

      /**
       * The transaction's confirmations.
       *
       * @return The confirmations
       */
      default IoCheckedScalar<Integer> confirmations() {
          return new IoCheckedScalar<>(this::getConfirmations);
      }

      /**
       * The transaction's confirmations.
       *
       * @return The confirmations
       */
      int getConfirmations();

      /**
       * The transaction's block hash.
       *
       * @return The block hash
       */
      default IoCheckedScalar<String> blockHash() {
          return new IoCheckedScalar<>(this::getBlockHash);
      }

      /**
       * The transaction's block hash.
       *
       * @return The block hash
       */
      String getBlockHash();

      /**
       * The transaction's block height.
       *
       * @return The block height
       */
      default IoCheckedScalar<Integer> blockHeight() {
          return new IoCheckedScalar<>(this::getBlockHeight);
      }

      /**
       * The transaction's block height.
       *
       * @return The block height
       */
      int getBlockHeight();

      /**
       * The transaction's error message.
       *
       * @return The error message
       */
      default IoCheckedScalar<String> errorMessage() {
          return new IoCheckedScalar<>(this::getErrorMessage);
      }

      /**
       * The transaction's error message.
       *
       * @return The error message
       */
      String getErrorMessage();

      /**
       * The transaction's confirmations required.
       *
       * @return The confirmations required
       */
      default IoCheckedScalar<Integer> confirmationsRequired() {
          return new IoCheckedScalar<>(this::getConfirmationsRequired);
      }

      /**
       * The transaction's confirmations required.
       *
       * @return The confirmations required
       */
      int getConfirmationsRequired();

      /**
       * The transaction's broadcast time.
       *
       * @return The broadcast time
       */
      default IoCheckedScalar<Long> broadcastTime() {
          return new IoCheckedScalar<>(this::getBroadcastTime);
      }

      /**
       * The transaction's broadcast time.
       *
       * @return The broadcast time
       */
      long getBroadcastTime();

      /**
       * The transaction's expiration time.
       *
       * @return The expiration time
       */
      default IoCheckedScalar<Long> expirationTime() {
          return new IoCheckedScalar<>(this::getExpirationTime);
      }

      /**
       * The transaction's expiration time.
       *
       * @return The expiration time
       */
      long getExpirationTime();

      /**
       * The transaction's gas price.
       *
       * @return The gas price
       */
      default IoCheckedScalar<Long> gasPrice() {
          return new IoCheckedScalar<>(this::getGasPrice);
      }

      /**
       * The transaction's gas price.
       *
       * @return The gas price
       */
      long getGasPrice();

      /**
       * The transaction's gas limit.
       *
       * @return The gas limit
       */
      default IoCheckedScalar<Long> gasLimit() {
          return new IoCheckedScalar<>(this::getGasLimit);
      }

      /**
       * The transaction's gas limit.
       *
       * @return The gas limit
       */
      long getGasLimit();

      /**
       * The transaction's nonce.
       *
       * @return The nonce
       */
      default IoCheckedScalar<Long> nonce() {
          return new IoCheckedScalar<>(this::getNonce);
      }

      /**
       * The transaction's nonce.
       *
       * @return The nonce
       */
      long getNonce();

      /**
       * The transaction's hash.
       *
       * @return The hash
       */
      default IoCheckedScalar<String> hash() {
          return new IoCheckedScalar<>(this::getHash);
      }

      /**
       * The transaction's hash.
       *
       * @return The hash
       */
      String getHash();

      /**
       * The transaction's index.
       *
       * @return The index
       */
      default IoCheckedScalar<Integer> index() {
          return new IoCheckedScalar<>(this::getIndex);
      }

      /**
       * The transaction's index.
       *
       * @return The index
       */
      int getIndex();

      /**
       * The transaction's inputs.
       *
       * @return The inputs
       */
      default IoCheckedScalar<List<RtTransactionInput>> inputs() {
          return new IoCheckedScalar<>(this::getInputs);
      }

      /**
       * The transaction's inputs.
       *
       * @return The inputs
       */
      List<RtTransactionInput> getInputs();

      /**
       * The transaction's outputs.
       *
       * @return The outputs
       */
      default IoCheckedScalar<List<RtTransactionOutput>> outputs() {
          return new IoCheckedScalar<>(this::getOutputs);
      }

      /**
       * The transaction's outputs.
       *
       * @return The outputs
       */
      List<RtTransactionOutput> getOutputs();

      /**
       * The transaction's confirmations required.
       *
       * @return The confirmations required
       */
      default IoCheckedScalar<Integer> confirmationsRequired() {
          return new IoCheckedScalar<>(this::getConfirmationsRequired);
      }

      /**
       * The transaction's confirmations required.
       *
       * @return The confirmations required
       */
      int getConfirmationsRequired();

      /**
       * The transaction's broadcast time.
       *
       * @return The broadcast time
       */
      default IoCheckedScalar<Long> broadcastTime() {
          return new IoCheckedScalar<>(this::getBroadcastTime);
      }

      /**
       * The transaction's broadcast time.
       *
       * @return The broadcast time
       */
      long getBroadcastTime();

      /**
       * The transaction's expiration time.
       *
       * @return The expiration time
       */
      default IoCheckedScalar<Long> expirationTime() {
          return new IoCheckedScalar<>(this::getExpirationTime);
      }

      /**
       * The transaction's expiration time.
       *
       * @return The expiration time
       */
      long getExpirationTime();

      /**
       * The transaction's gas price.
       *
       * @return The gas price
       */
      default IoCheckedScalar<Long> gasPrice() {
          return new IoCheckedScalar<>(this::getGasPrice);
      }

      /**
       * The transaction's gas price.
       *
       * @return The gas price
       */
      long getGasPrice();

      /**
       * The transaction's gas limit.
       *
       * @return The gas limit
       */
      default IoCheckedScalar<Long> gasLimit() {
          return new IoCheckedScalar<>(this::getGasLimit);
      }

      /**
       * The transaction's gas limit.
       *
       * @return The gas limit
       */
      long getGasLimit();

      /**
       * The transaction's nonce.
       *
       * @return The nonce
       */
      default IoCheckedScalar<Long> nonce() {
          return new IoCheckedScalar<>(this::getNonce);
      }

      /**
       * The transaction's nonce.
       *
       * @return The nonce
       */
      long getNonce();

      /**
       * The transaction's hash.
       *
       * @return The hash
       */
      default IoCheckedScalar<String> hash() {
          return new IoCheckedScalar<>(this::getHash);
      }

      /**
       * The transaction's hash.
       *
       * @return The hash
       */
      String getHash();

      /**
       * The transaction's index.
       *
       * @return The index
       */
      default IoCheckedScalar<Integer> index() {
          return new IoCheckedScalar<>(this::getIndex);
      }

      /**
       * The transaction's index.
       *
       * @return The index
       */
      int getIndex();

      /**
       * The transaction's inputs.
       *
       * @return The inputs
       */
      default IoCheckedScalar<List<RtTransactionInput>> inputs() {
          return new IoCheckedScalar<>(this::getInputs);
      }

      /**
       * The transaction's inputs.
       *
       * @return The inputs
       */
      List<RtTransactionInput> getInputs();

      /**
       * The transaction's outputs.
       *
       * @return The outputs
       */
      default IoCheckedScalar<List<RtTransactionOutput>> outputs() {
          return new IoCheckedScalar<>(this::getOutputs);
      }

      /**
       * The transaction's outputs.
       *
       * @return The outputs
       */
      List<RtTransactionOutput> getOutputs();
  }
```