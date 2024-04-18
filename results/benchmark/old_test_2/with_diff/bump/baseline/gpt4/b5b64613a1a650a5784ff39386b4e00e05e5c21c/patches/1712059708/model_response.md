```java
import org.apache.commons.lang3.StringUtils;

public class CreateJFrogInstanceStep {
    public boolean isAllBlank(String... css) {
        return StringUtils.isAllEmpty(css);
    }
}
```