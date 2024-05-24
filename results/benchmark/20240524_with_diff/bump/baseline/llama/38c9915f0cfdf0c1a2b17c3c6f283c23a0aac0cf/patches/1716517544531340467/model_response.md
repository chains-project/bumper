```java
import org.cactoos.scalar.Solid;

SolidScalar scalar = new Solid(new ScalarOf(new Runnable() {
    public void run() {
        // empty
    }
}));
```