```java
import java.text.MessageFormat;

public class FormattedText {
    public static String format(String pattern, Object... arguments) {
        return MessageFormat.format(pattern, arguments);
    }
}
```