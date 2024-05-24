```java
import org.apache.commons.lang3.StringUtils;

public class MyClient {

    public void myMethod() {
        String text = "  ";
        if (StringUtils.isBlank(text)) {
            // Do something
        }
    }
}
```