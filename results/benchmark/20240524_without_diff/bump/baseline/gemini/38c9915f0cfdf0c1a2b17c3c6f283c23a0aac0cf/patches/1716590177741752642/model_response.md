```java
import org.cactoos.text.SplitText;
import java.util.Arrays;

public class RtTransaction {

    public String[] getOutputs() {
        return new SplitText(this.getOutputsString()).asArray();
    }

}
```