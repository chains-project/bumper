```
import java.text.MessageFormat;

public class WalletsIn {
    public static void main(String[] args) {
        String text = "Hello, {0}!";
        String formattedText = new MessageFormat(text).format(new Object[] { "world" });
        System.out.println(formattedText);
    }
}
```