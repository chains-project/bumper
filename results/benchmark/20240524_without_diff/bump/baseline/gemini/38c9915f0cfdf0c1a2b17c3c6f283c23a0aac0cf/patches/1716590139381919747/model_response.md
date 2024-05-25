```java
import org.cactoos.text.SplitText;
import java.util.List;

public class RtTransaction {

    public List<String> splitString(String string, String regex) {
        return new SplitText(string, regex).asList();
    }
}
```