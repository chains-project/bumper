The error message indicates that the symbol `LengthOf` cannot be found. This is likely due to the fact that the dependency `org.cactoos.iterable.LengthOf` no longer exists or has been moved to a different package. 

Unfortunately, without knowing the new location or the replacement of `LengthOf` class in the updated dependency, it's impossible to provide a specific solution. 

However, a general solution would be to find the replacement of the `LengthOf` class in the updated version of the dependency and import that instead. For example, if the `LengthOf` class has been moved to `org.cactoos.collection.LengthOf`, the import statement would be updated as follows:

```java
import org.cactoos.collection.LengthOf;
```

If the `LengthOf` class has been removed entirely, you would need to find a replacement functionality within the updated dependency and use that instead. Without knowing the specifics of the dependency update, it's impossible to provide a more specific solution.

Please check the updated dependency documentation to find the replacement of `LengthOf` class.