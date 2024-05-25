```java
import org.cactoos.text.SplitText;
import java.util.List;

public class RtTransaction {

    public List<String> split(String text, String delimiter) {
        return new SplitText(text, delimiter).asList();
    }
}
```