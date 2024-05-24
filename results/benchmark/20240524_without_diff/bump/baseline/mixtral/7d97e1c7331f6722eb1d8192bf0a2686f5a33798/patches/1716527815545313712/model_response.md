Here's a patch that should fix the error:

```java
import com.jcabi.aspects.Immutable;

@Immutable
public class RegionITCase {
  // ...
}
```

In the updated library version, the `Tv` class has been removed and its functionality has been moved to the `Immutable` aspect. Therefore, we can replace the `Tv` import with `Immutable` and add the `@Immutable` annotation to the class to achieve the same behavior.