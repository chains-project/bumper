```java
import java.util.Arrays;

public boolean isAllBlank(String... strs) {
    for (String str : strs) {
        if (!str.trim().isEmpty()) {
            return false;
        }
    }
    return true;
}
```