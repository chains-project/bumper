```java
import org.cactoos.scalar.Sticky;

StickyScalar stickyScalar = new Sticky(new ScalarOf(new Runnable() {
    public void run() {
        // implementation
    }
}));
```