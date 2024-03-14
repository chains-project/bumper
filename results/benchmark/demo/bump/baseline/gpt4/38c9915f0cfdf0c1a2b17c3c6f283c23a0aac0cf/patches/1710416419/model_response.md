The error message indicates that the symbol `IoCheckedScalar` cannot be found. This means that the import statement is incorrect. There might be a change in the library where the `IoCheckedScalar` class is no longer available or it has been moved to another package.

In this scenario, since we cannot change the external library and we don't have information about the changes in the library, the best approach would be to use an alternative class that provides similar functionality.

Here is a patch that you can apply:

```java
  import org.cactoos.scalar.CheckedScalar;
```

Please note that you will need to update your code to use `CheckedScalar` instead of `IoCheckedScalar`. If `CheckedScalar` doesn't have the same methods that were available in `IoCheckedScalar`, you may need to adjust your code accordingly.