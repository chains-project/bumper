```java
import org.apache.commons.lang3.StringUtils;

public class Main {
    public boolean test(String... args) {
        return StringUtils.isBlank(args[0]) && StringUtils.isBlank(args[1]);
    }
}
```