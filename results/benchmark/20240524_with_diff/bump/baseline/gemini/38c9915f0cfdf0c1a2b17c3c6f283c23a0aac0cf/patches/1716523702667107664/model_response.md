```java
import org.cactoos.scalar.LengthOf;

import java.util.Iterator;

public class RtScore {

    // ...

    public RtScore(Iterator<Double> scores) {
        this(new LengthOf(scores));
    }

    // ...

}
```