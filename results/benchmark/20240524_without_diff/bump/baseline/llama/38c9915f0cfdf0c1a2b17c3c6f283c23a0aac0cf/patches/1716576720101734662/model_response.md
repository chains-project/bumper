```java
import java.text.Normalizer;

public class UncheckedText {
    public static String normalize(String text) {
        return Normalizer.normalize(text, Normalizer.Form.NFKD);
    }
}
```