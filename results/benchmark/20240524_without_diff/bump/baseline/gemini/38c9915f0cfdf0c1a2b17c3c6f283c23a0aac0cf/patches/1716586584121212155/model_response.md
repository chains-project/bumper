```java
import org.cactoos.text.TextOf;
import org.cactoos.iterable.IterableOf;

import java.util.List;
import java.util.ArrayList;

public class RtScore {

    public List<Integer> calculate(List<Integer> scores) {
        int minScore = 0;
        int maxScore = 0;
        int sum = 0;
        int count = 0;

        for (int score : scores) {
            minScore = Math.min(minScore, score);
            maxScore = Math.max(maxScore, score);
            sum += score;
            count++;
        }

        List<Integer> result = new ArrayList<>();
        result.add(minScore);
        result.add(maxScore);
        result.add(sum / count);
        return result;
    }
}
```