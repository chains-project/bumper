```java
import java.util.Objects;

public boolean isAllBlank(String... strs) {
    for (String str : strs) {
        if (!Objects.requireNonNull(str).trim().isEmpty()) {
            return false;
        }
    }
    return true;
}
```