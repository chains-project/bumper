```java
import java.util.Arrays;

public boolean isAllBlank(String... strings) {
    for (String str : strings) {
        if (!str.trim().isEmpty()) {
            return false;
        }
    }
    return true;
}
```