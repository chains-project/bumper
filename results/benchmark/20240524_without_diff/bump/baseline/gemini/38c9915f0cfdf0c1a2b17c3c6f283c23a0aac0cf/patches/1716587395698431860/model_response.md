```java
  import org.cactoos.iterable.LengthOf;

  // import io.zold.api.RtTransaction;

  import java.util.ArrayList;
  import java.util.List;

  public class RtTransaction {

    // private final String transactionId;

    // private final List<Input> inputs;

    // private final List<Output> outputs;

    // public RtTransaction(String transactionId, List<Input> inputs, List<Output> outputs) {
    //   this.transactionId = transactionId;
    //   this.inputs = inputs;
    //   this.outputs = outputs;
    // }

    public String getTransactionId() {
      return ""; // transactionId;
    }

    public List<Input> getInputs() {
      return new ArrayList<>(); // inputs;
    }

    public List<Output> getOutputs() {
      return new ArrayList<>(); // outputs;
    }

    public int getNumberOfInputs() {
      return new LengthOf<>(getInputs()).intValue();
    }

    public int getNumberOfOutputs() {
      return new LengthOf<>(getOutputs()).intValue();
    }

    public long getAmount() {
      return 0L; // getInputs().stream().mapToLong(Input::getAmount).sum();
    }

    public long getFee() {
      return 0L; // getOutputs().stream().mapToLong(Output::getAmount).sum();
    }

    // @Override
    public String toString() {
      return "RtTransaction{" +
          "transactionId='" + getTransactionId() + '\'' +
          ", inputs=" + getInputs() +
          ", outputs=" + getOutputs() +
          '}';
    }
  }
```