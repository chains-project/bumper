```java
import java.util.Arrays;

public boolean isAllBlank(String... strs) {
    return Arrays.stream(strs).allMatch(String::isBlank);
}
```