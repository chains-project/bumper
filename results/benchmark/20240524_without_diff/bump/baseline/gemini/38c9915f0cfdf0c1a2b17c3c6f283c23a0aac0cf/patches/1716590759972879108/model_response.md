```java
  import org.cactoos.text.TextOf;

  public final class RtTransaction {
    public RtTransaction(String rtTransactionId, String rtTransactionType, String rtTransactionStatus, String rtTransactionDate, String rtTransactionAmount, String rtTransactionCurrency, String rtTransactionDescription, String rtTransactionReference, String rtTransactionSource, String rtTransactionDestination) {
      this.rtTransactionId = rtTransactionId;
      this.rtTransactionType = rtTransactionType;
      this.rtTransactionStatus = rtTransactionStatus;
      this.rtTransactionDate = rtTransactionDate;
      this.rtTransactionAmount = rtTransactionAmount;
      this.rtTransactionCurrency = rtTransactionCurrency;
      this.rtTransactionDescription = rtTransactionDescription;
      this.rtTransactionReference = rtTransactionReference;
      this.rtTransactionSource = rtTransactionSource;
      this.rtTransactionDestination = rtTransactionDestination;
    }

    private final String rtTransactionId;
    private final String rtTransactionType;
    private final String rtTransactionStatus;
    private final String rtTransactionDate;
    private final String rtTransactionAmount;
    private final String rtTransactionCurrency;
    private final String rtTransactionDescription;
    private final String rtTransactionReference;
    private final String rtTransactionSource;
    private final String rtTransactionDestination;

    public String getRtTransactionId() {
      return rtTransactionId;
    }

    public String getRtTransactionType() {
      return rtTransactionType;
    }

    public String getRtTransactionStatus() {
      return rtTransactionStatus;
    }

    public String getRtTransactionDate() {
      return rtTransactionDate;
    }

    public String getRtTransactionAmount() {
      return rtTransactionAmount;
    }

    public String getRtTransactionCurrency() {
      return rtTransactionCurrency;
    }

    public String getRtTransactionDescription() {
      return rtTransactionDescription;
    }

    public String getRtTransactionReference() {
      return rtTransactionReference;
    }

    public String getRtTransactionSource() {
      return rtTransactionSource;
    }

    public String getRtTransactionDestination() {
      return rtTransactionDestination;
    }

    @Override
    public String toString() {
      return new TextOf(
          "RtTransaction{" +
              "rtTransactionId='" + rtTransactionId + '\'' +
              ", rtTransactionType='" + rtTransactionType + '\'' +
              ", rtTransactionStatus='" + rtTransactionStatus + '\'' +
              ", rtTransactionDate='" + rtTransactionDate + '\'' +
              ", rtTransactionAmount='" + rtTransactionAmount + '\'' +
              ", rtTransactionCurrency='" + rtTransactionCurrency + '\'' +
              ", rtTransactionDescription='" + rtTransactionDescription + '\'' +
              ", rtTransactionReference='" + rtTransactionReference + '\'' +
              ", rtTransactionSource='" + rtTransactionSource + '\'' +
              ", rtTransactionDestination='" + rtTransactionDestination + '\'' +
              '}'
      ).asString();
    }
  }
```