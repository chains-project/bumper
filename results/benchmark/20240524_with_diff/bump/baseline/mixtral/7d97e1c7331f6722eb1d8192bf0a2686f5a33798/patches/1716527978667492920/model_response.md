Here's the proposed patch for the failing client code:

```java
import com.jcabi.aspects.Loggable;

@Loggable(Loggable.DEBUG)
public class RegionITCase {
  // existing code...
}
```

The `Tv` class has been removed in the new library version, but the `Loggable` aspect can be used instead. I've added the `@Loggable` annotation with the `DEBUG` level to the `RegionITCase` class. You can adjust the logging level according to your needs.