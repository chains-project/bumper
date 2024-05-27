The provided code is an import statement, it cannot exist on its own without a class, interface or enum. It seems like there might be a misunderstanding here as an import statement alone can't be the cause of the error message you're seeing.

However, here is a simple class example using the import statement:

```java
import static org.junit.jupiter.api.Assertions.assertEquals;

public class PGS_MorphologyGroupShapeTests {

    @org.junit.jupiter.api.Test
    public void test() {
        int expected = 5;
        int actual = 2 + 3;
        assertEquals(expected, actual);
    }
}
```