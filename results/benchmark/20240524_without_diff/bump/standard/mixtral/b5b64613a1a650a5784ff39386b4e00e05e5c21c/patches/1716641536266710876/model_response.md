Here's the proposed patch for the client code:

```java
import java.util.Objects;

// ...

if (Objects.isNull(jfrogInstance)) {
  // ...
}
```

The `isNull` method from `java.util.Objects` should be accessed using the fully qualified name instead of the static import.