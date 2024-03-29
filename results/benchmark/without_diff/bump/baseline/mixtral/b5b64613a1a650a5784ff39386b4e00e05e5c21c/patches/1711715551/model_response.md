Here is a fixed version of the method that should resolve the error:
```java
import static org.apache.commons.lang3.StringUtils.isBlank;

@Override
public CreateJFrogInstanceStep execute(StepContext context) throws IOException, InterruptedException {
    // existing code
    if (isBlank(jfrogInstanceId) || isBlank(url) || isBlank(apiKey)) {
        // existing code
    }
    // existing code
}
```
In this version, I replaced the usage of `isAllBlank` with `isBlank`, which is still present in the `org.apache.commons.lang3.StringUtils` class. This should resolve the "cannot find symbol" error.