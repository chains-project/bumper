```java
import java.util.Arrays;

public boolean isAllBlank(String... strings) {
    return Arrays.stream(strings).allMatch(String::isBlank);
}
```