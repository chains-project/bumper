```java
import org.apache.commons.lang3.StringUtils;

public class Fix {
    public void method() {
        boolean isNotBlank = StringUtils.isNotBlank(null);
    }
}
```