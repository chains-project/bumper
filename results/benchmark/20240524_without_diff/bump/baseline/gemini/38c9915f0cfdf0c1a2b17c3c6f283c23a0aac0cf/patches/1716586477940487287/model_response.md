```java
  import org.cactoos.iterable.LengthOf;

  import java.util.Iterator;

  public class RtScore {
      public static int rtScore(Iterator<Integer> scores) {
          int score = 0;
          while (scores.hasNext()) {
              score += scores.next();
          }
          return score;
      }
  }
```