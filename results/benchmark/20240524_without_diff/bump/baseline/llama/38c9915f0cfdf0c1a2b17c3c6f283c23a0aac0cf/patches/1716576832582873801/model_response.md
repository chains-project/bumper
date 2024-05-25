```java
import java.io.IOException;
import java.io.StringReader;
import java.io.StringWriter;

public class UncheckedText {
    public static String asString(String text) throws IOException {
        StringWriter writer = new StringWriter();
        StringReader reader = new StringReader(text);
        int ch;
        while ((ch = reader.read()) != -1) {
            writer.write(ch);
        }
        return writer.toString();
    }
}
```