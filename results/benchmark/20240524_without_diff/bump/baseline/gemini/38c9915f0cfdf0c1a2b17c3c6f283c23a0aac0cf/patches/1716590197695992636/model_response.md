```java
  import org.cactoos.text.SplitText;

  import java.util.ArrayList;
  import java.util.List;

  public class RtTransaction {

    // ...

    @Override
    public List<String> getOutputs() {
      List<String> outputs = new ArrayList<>();
      for (String output : new SplitText(this.output).asString()) {
        outputs.add(output);
      }
      return outputs;
    }

    // ...
  }
```