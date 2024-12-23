```java
  import org.cactoos.scalar.ItemAt;
  import org.cactoos.scalar.LengthOf;

  public class RtTransaction {
    public static final String TRANSACTION_ID = "transactionId";
    public static final String TRANSACTION_TIME = "transactionTime";
    public static final String TRANSACTION_TYPE = "transactionType";
    public static final String TRANSACTION_AMOUNT = "transactionAmount";
    public static final String TRANSACTION_CURRENCY = "transactionCurrency";
    public static final String TRANSACTION_FEE = "transactionFee";
    public static final String TRANSACTION_STATUS = "transactionStatus";
    public static final String TRANSACTION_DETAILS = "transactionDetails";
    public static final String TRANSACTION_ERROR_CODE = "transactionErrorCode";
    public static final String TRANSACTION_ERROR_MESSAGE = "transactionErrorMessage";
    public static final String TRANSACTION_HASH = "transactionHash";
    public static final String TRANSACTION_BLOCK_NUMBER = "transactionBlockNumber";
    public static final String TRANSACTION_CONFIRMATIONS = "transactionConfirmations";
    public static final String TRANSACTION_SENDER = "transactionSender";
    public static final String TRANSACTION_RECIPIENT = "transactionRecipient";
    public static final String TRANSACTION_CONTRACT_ADDRESS = "transactionContractAddress";
    public static final String TRANSACTION_GAS_USED = "transactionGasUsed";
    public static final String TRANSACTION_GAS_PRICE = "transactionGasPrice";
    public static final String TRANSACTION_GAS_LIMIT = "transactionGasLimit";
    public static final String TRANSACTION_NONCE = "transactionNonce";
    public static final String TRANSACTION_INPUT = "transactionInput";
    public static final String TRANSACTION_OUTPUT = "transactionOutput";
    public static final String TRANSACTION_LOGS = "transactionLogs";

    private final Map<String, Object> data;

    public RtTransaction(Map<String, Object> data) {
      this.data = data;
    }

    public String getTransactionId() {
      return (String) data.get(TRANSACTION_ID);
    }

    public long getTransactionTime() {
      return (long) data.get(TRANSACTION_TIME);
    }

    public String getTransactionType() {
      return (String) data.get(TRANSACTION_TYPE);
    }

    public BigDecimal getTransactionAmount() {
      return (BigDecimal) data.get(TRANSACTION_AMOUNT);
    }

    public String getTransactionCurrency() {
      return (String) data.get(TRANSACTION_CURRENCY);
    }

    public BigDecimal getTransactionFee() {
      return (BigDecimal) data.get(TRANSACTION_FEE);
    }

    public String getTransactionStatus() {
      return (String) data.get(TRANSACTION_STATUS);
    }

    public Map<String, Object> getTransactionDetails() {
      return (Map<String, Object>) data.get(TRANSACTION_DETAILS);
    }

    public String getTransactionErrorCode() {
      return (String) data.get(TRANSACTION_ERROR_CODE);
    }

    public String getTransactionErrorMessage() {
      return (String) data.get(TRANSACTION_ERROR_MESSAGE);
    }

    public String getTransactionHash() {
      return (String) data.get(TRANSACTION_HASH);
    }

    public long getTransactionBlockNumber() {
      return (long) data.get(TRANSACTION_BLOCK_NUMBER);
    }

    public long getTransactionConfirmations() {
      return (long) data.get(TRANSACTION_CONFIRMATIONS);
    }

    public String getTransactionSender() {
      return (String) data.get(TRANSACTION_SENDER);
    }

    public String getTransactionRecipient() {
      return (String) data.get(TRANSACTION_RECIPIENT);
    }

    public String getTransactionContractAddress() {
      return (String) data.get(TRANSACTION_CONTRACT_ADDRESS);
    }

    public long getTransactionGasUsed() {
      return (long) data.get(TRANSACTION_GAS_USED);
    }

    public BigDecimal getTransactionGasPrice() {
      return (BigDecimal) data.get(TRANSACTION_GAS_PRICE);
    }

    public long getTransactionGasLimit() {
      return (long) data.get(TRANSACTION_GAS_LIMIT);
    }

    public long getTransactionNonce() {
      return (long) data.get(TRANSACTION_NONCE);
    }

    public String getTransactionInput() {
      return (String) data.get(TRANSACTION_INPUT);
    }

    public String getTransactionOutput() {
      return (String) data.get(TRANSACTION_OUTPUT);
    }

    public List<Map<String, Object>> getTransactionLogs() {
      return (List<Map<String, Object>>) data.get(TRANSACTION_LOGS);
    }

    @Override
    public String toString() {
      return "RtTransaction{" +
          "data=" + data +
          '}';
    }
  }
```