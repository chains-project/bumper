```java
import java.util.Arrays;

public boolean isAllBlank(String... strs) {
    for (String str : strs) {
        if (str != null && !str.trim().isEmpty()) {
            return false;
        }
    }
    return true;
}
```