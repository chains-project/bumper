```java
import java.util.Arrays;

public boolean isAllBlank(String... strings) {
    for (String string : strings) {
        if (string != null && !string.trim().isEmpty()) {
            return false;
        }
    }
    return true;
}
```