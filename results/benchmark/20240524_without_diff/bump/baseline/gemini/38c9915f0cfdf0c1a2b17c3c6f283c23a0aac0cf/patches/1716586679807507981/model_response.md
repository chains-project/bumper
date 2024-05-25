```java
import org.cactoos.iterable.LengthOf;

import java.util.List;

public class RtScore {

    public static double calculate(List<Double> scores) {
        if (scores == null || scores.isEmpty()) {
            return 0.0;
        }

        double sum = 0.0;
        for (double score : scores) {
            sum += score;
        }

        return sum / new LengthOf<>(scores).value();
    }
}
```