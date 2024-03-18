It seems like the package or class `org.cactoos.scalar.IoCheckedScalar` does not exist or is not accessible from the current package. 

If the class is not available in the new version of the dependency, you may need to use an alternative class or method that provides the same functionality. 

Unfortunately, without more information about the use of `IoCheckedScalar` in your code and the available classes in the new version of the dependency, it's impossible to provide a more specific solution. 

If `org.cactoos.scalar.IoCheckedScalar` has been moved to another package, you will need to update the import statement to reflect the new package name. 

For example, if `IoCheckedScalar` has been moved to the `org.cactoos.scalar.newpackage` package, you would change the import statement to:

```java
import org.cactoos.scalar.newpackage.IoCheckedScalar;
```

If `IoCheckedScalar` has been renamed or replaced by another class, you would need to update the import statement and any usage of `IoCheckedScalar` in your code to use the new class name. 

For example, if `IoCheckedScalar` has been replaced by `NewScalar` in the `org.cactoos.scalar` package, you would change the import statement to:

```java
import org.cactoos.scalar.NewScalar;
```

And update any usage of `IoCheckedScalar` in your code to `NewScalar`.