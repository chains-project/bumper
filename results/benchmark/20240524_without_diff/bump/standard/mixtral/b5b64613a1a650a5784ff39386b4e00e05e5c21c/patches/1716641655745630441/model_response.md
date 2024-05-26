Here is the proposed patch for the failing client code:

```java
import java.util.Objects;

// ...

if (isNull(jfrogInstance)) {
    // ...
}
```

The `isNull` method is now imported from `java.util.Objects` instead of using a static import.