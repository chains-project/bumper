As the error message indicates, the class `TrimmedText` could not be found in the package `org.cactoos.text`. This is likely due to a change in the library where the `TrimmedText` class was removed or moved to a different package.

However, without the specific changes in the library, I cannot provide an exact solution. Generally, you would need to find an equivalent class or method in the new library version and replace the `TrimmedText` with it.

For example, if there is a new class `TrimText` in the same package that performs the same function, you would replace `TrimmedText` with `TrimText` like so:

```java
import org.cactoos.text.TrimText;
```

If the class was moved to a different package, you would update the import statement with the new package. For example, if `TrimmedText` was moved to `org.cactoos.string`, you would do:

```java
import org.cactoos.string.TrimmedText;
```

Please provide the specific library changes so I can give a more accurate solution.