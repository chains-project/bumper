```java
import org.junit.internal.AssumptionViolatedException;
import org.junit.internal.runners.model.MultipleFailureException;

public class FastPolygonizerTests {
    public void test() {
        throw new AssumptionViolatedException("Ignored");
    }
}
```