Here's a proposed patch to fix the error:
```
import static org.apache.commons.lang3.StringUtils.isAllBlank;

// Replace the failing line with the following code
import org.apache.commons.lang3.StringUtils;

public class CreateJFrogInstanceStep extends Step {
    // ...
}
```
The patch imports the `StringUtils` class from the `org.apache.commons.lang3` package, which contains the `isAllBlank` method. This allows the code to compile without the error.