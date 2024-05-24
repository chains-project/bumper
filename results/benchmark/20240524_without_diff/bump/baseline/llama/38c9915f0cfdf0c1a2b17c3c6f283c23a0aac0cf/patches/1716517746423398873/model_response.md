```
import org.cactoos.scalar.Unchecked;

UncheckedScalar scalar = new Unchecked(new ScalarOf(new Runnable() {
    public void run() {
        // your code here
    }
}));
```