```java
import org.cactoos.Text;
import org.cactoos.text.TextOf;

Text randomText = new TextOf(
    new Random().ints(48, 122)
        .filter(i -> (i < 57 || i > 65) && (i < 90 || i > 97))
        .mapToObj(i -> (char) i)
        .limit(10)
        .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
        .toString()
);
```