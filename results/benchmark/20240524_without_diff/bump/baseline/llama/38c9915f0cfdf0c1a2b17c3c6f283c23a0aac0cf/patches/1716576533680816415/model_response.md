```java
import java.io.IOException;

import org.cactoos.Scalar;

public class IoCheckedScalar implements Scalar<Boolean> {
    private final Scalar<Boolean> origin;

    public IoCheckedScalar(Scalar<Boolean> origin) {
        this.origin = origin;
    }

    @Override
    public Boolean value() throws IOException {
        return origin.value();
    }
}
```