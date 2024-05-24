```java
import org.apache.commons.lang3.StringUtils;

public class Main {
    public static void main(String[] args) {
        boolean result = StringUtils.isNotBlank(null);
        System.out.println(result);
    }
}
```