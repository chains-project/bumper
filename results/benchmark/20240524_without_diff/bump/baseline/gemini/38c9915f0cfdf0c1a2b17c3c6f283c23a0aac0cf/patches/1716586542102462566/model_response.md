```java
import org.cactoos.iterable.LengthOf;
import java.util.List;

public class RtScore {
    private final List<Double> scores;

    public RtScore(List<Double> scores) {
        this.scores = scores;
    }

    public double calculate() {
        if (new LengthOf(scores).value() == 0) {
            return 0;
        }
        double sum = 0;
        for (double score : scores) {
            sum += score;
        }
        return sum / scores.size();
    }
}
```