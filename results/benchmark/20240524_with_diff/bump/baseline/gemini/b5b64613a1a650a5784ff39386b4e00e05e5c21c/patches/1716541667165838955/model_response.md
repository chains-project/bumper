```java
import static org.apache.commons.lang3.StringUtils.isNotBlank;

public class CreateJFrogInstanceStep {

    public void step(Map<String, Object> binding) {
        // ...

        if (isNotBlank(artifactoryUrl)) {
            // ...
        }

        // ...
    }
}
```