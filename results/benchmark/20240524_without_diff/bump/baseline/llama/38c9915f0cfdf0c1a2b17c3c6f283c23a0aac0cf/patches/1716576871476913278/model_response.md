```java
import java.text.Normalizer;

public class WalletsIn {
    public void method() {
        String normalized = Normalizer.normalize("some text", Normalizer.Form.NFKC);
    }
}
```