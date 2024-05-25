```java
  import org.cactoos.Text;
  import org.cactoos.text.TextOf;
  import java.util.Random;

  Text randomText = new TextOf(new Random().ints(48, 123)
    .filter(i -> (i <= 57 || i >= 65) && (i <= 90 || i >= 97))
    .limit(10)
    .collect(StringBuilder::new, StringBuilder::appendCodePoint, StringBuilder::append)
    .toString());
```