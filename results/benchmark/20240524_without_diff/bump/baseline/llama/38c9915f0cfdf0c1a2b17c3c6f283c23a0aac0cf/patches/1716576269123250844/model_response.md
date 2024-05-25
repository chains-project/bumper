```java
import java.util.stream.Stream;
import java.util.Arrays;

String[] texts = {"text1", "text2", "text3"};
String joinedText = Arrays.stream(texts).reduce((a, b) -> a + ", " + b).orElse("");
```