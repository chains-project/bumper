This error message is indicating that the import statement is outside the class declaration. You can't have import statements in the middle of your code, they must be at the top of the file. Here is the corrected code:

```java
import org.junit.jupiter.api.Test;

public class PGS_MorphologyGroupShapeTests {
  // rest of your class code here
}
```