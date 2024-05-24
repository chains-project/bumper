```java
import org.cactoos.scalar.Solid;

SolidScalar solidScalar = new Solid(new ScalarOf(new Runnable() {
    public void run() {
        // No-op
    }
}));
```