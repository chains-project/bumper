Here's a patch that should fix the error:
```java
import org.junit.jupiter.api.BeforeEach;

public class YourClass {
    // other class members

    @BeforeEach
    public void setup() {
        // initialize dependencies
    }

    public void yourMethod() {
        // your method implementation

        // use the new size() method from the updated library
        int size = new org.tinspin.index.PointIndexMMWrapper().size();

        // rest of your method implementation
    }
}
```
Note that you'll need to replace `YourClass` and `yourMethod` with the actual class and method names in your code. Also, you may need to adjust the argument to the `size()` method depending on your specific use case.