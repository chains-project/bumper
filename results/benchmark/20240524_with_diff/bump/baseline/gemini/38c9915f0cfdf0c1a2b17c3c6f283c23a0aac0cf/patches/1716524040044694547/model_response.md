```java
import org.cactoos.text.TextOfScalar;

public class WalletsIn {

    public static void main(String[] args) {
        String text = new TextOfScalar("Hello, world!").asString();
        System.out.println(text);
    }
}
```