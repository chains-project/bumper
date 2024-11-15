```java
import org.cactoos.iterable.LengthOf;

import java.util.List;

public class RtScore {
    private final List<Double> scores;

    public RtScore(List<Double> scores) {
        this.scores = scores;
    }

    public double get() {
        if (scores.isEmpty()) {
            return 0.0;
        }
        double sum = 0.0;
        for (double score : scores) {
            sum += score;
        }
        return sum / scores.size();
    }

    public double get(int index) {
        if (index < 0 || index >= scores.size()) {
            throw new IndexOutOfBoundsException("Index: " + index + ", Size: " + scores.size());
        }
        return scores.get(index);
    }

    public int length() {
        return scores.size();
    }

    public boolean isEmpty() {
        return scores.isEmpty();
    }

    public List<Double> asList() {
        return scores;
    }
}
```