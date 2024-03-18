The error message you're receiving is indicating that the symbol `IoCheckedScalar` cannot be found. This could be due to a couple of reasons:

1. The import statement is incorrect, or the package `org.cactoos.scalar` doesn't contain `IoCheckedScalar`.
2. The library `org.cactoos` is not correctly added to the project.

However, since I'm not allowed to modify the dependencies, I'll assume that the library is correctly added and the issue lies within the import statement. You should check the correct package for `IoCheckedScalar`. For the sake of this example, let's assume that it's located in `org.cactoos.Scalar` instead of `org.cactoos.scalar`.

Here's the corrected import statement:

```java
import org.cactoos.Scalar.IoCheckedScalar;
```

Please replace your current import statement with the above one. If `IoCheckedScalar` is located in a different package, adjust the import statement accordingly.