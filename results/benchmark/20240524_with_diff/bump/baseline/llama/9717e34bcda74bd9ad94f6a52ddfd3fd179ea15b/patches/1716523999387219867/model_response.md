```java
import com.jcabi.aoc.annotations.AutoInject;
import com.jcabi.aoc.annotations.AutoWire;

@AutoWire
public class MkGithub {
    @AutoInject
    private Github github;

    // ...
}
```