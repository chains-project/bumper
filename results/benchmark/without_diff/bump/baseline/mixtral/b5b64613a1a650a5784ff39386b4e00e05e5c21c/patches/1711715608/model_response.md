Here is a fixed version of the method that should resolve the error:
```java
import static org.apache.commons.lang3.StringUtils.isBlank;

@Override
public CreateJFrogInstanceStep extendedBehavior(StepContext context) {
    if (context == null || isBlank(serverId) || isBlank(repository)) {
        throw new InvalidRequestException("Missing parameters to create JFrog instance.");
    }
    return this;
}
```
In this version, I replaced the usage of `isAllBlank` with `isBlank`, which is still present in the `org.apache.commons.lang3.StringUtils` class. This should resolve the "cannot find symbol" error.