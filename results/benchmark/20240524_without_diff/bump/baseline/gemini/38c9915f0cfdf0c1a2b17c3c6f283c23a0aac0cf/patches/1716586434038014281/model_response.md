```java
import org.cactoos.iterable.LengthOf;
import org.cactoos.iterable.Mapped;

import java.util.Iterator;

public class RtScore {

    private final int score;

    public RtScore(int score) {
        this.score = score;
    }

    public int getScore() {
        return score;
    }

    public static RtScore of(String score) {
        if (score == null || score.isEmpty()) {
            return new RtScore(0);
        }

        Iterator<String> iterator = new LengthOf(score).iterator();

        int result = 0;
        while (iterator.hasNext()) {
            String digit = iterator.next();
            result = result * 10 + Integer.parseInt(digit);
        }

        return new RtScore(result);
    }
}
```