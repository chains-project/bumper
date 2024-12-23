```java
import org.cactoos.iterable.LengthOf;
import java.util.List;

public class RtScore {

    /**
     * Calculates the Rt score for a given list of cases.
     *
     * @param cases the list of cases
     * @return the Rt score
     */
    public double calculateRt(List<Case> cases) {
        // Calculate the number of new cases in the last 7 days.
        int newCases = new LengthOf<>(cases.subList(cases.size() - 7, cases.size())).intValue();

        // Calculate the number of new cases in the previous 7 days.
        int previousNewCases = new LengthOf<>(cases.subList(cases.size() - 14, cases.size() - 7)).intValue();

        // Calculate the Rt score.
        return (double) newCases / previousNewCases;
    }
}
```