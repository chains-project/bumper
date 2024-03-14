It appears that the error is due to the inability to find the symbol `IoCheckedScalar`. This could be due to the symbol being removed from the `org.cactoos.scalar` package in a recent update. 

Unfortunately, without more context or information about the rest of the code, it's impossible to provide a specific fix. However, a general approach would be to replace the usage of `IoCheckedScalar` with another class or method that provides similar functionality. 

For example, if `IoCheckedScalar` was used to handle exceptions, you might replace it with `UncheckedScalar` (if it's available in the updated dependency) or use a try-catch block.

Here's a hypothetical patch, assuming that `IoCheckedScalar` was used as a type for a variable `scalar`:

```java
import org.cactoos.scalar.UncheckedScalar;

// rest of the code

UncheckedScalar scalar;

// rest of the code
```

Please note that this is a hypothetical solution. The actual solution may vary depending on the usage of `IoCheckedScalar` and the available classes/methods in the updated `org.cactoos.scalar` package.