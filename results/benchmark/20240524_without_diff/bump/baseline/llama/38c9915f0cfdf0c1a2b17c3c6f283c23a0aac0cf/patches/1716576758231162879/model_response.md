```java
import java.text.Normalizer;

public class WalletsIn {
    public String walletsIn() {
        return Normalizer.normalize("some text", Normalizer.Form.NFKC);
    }
}
```