```java
import java.util.stream.Stream;

public boolean isAllBlank(String... strs) {
    return Stream.of(strs).allMatch(String::isBlank);
}
```