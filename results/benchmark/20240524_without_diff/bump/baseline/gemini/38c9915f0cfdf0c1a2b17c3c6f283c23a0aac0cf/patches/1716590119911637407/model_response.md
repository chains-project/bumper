```java
  import org.cactoos.text.SplitText;

  import java.util.List;
  import java.util.stream.Collectors;

  public class RtTransaction {

      public static List<String> split(String text) {
          return new SplitText(text).stream().collect(Collectors.toList());
      }

      // ...
  }
```