```java
import java.util.Arrays;
import java.util.stream.Stream;

String joined = Stream.of("part1", "part2", "part3")
        .reduce((a, b) -> a + ", " + b)
        .orElse("");
```