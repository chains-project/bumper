It seems like the import statement is failing because the class `IoCheckedScalar` cannot be found in the `org.cactoos.scalar` package. This could be due to various reasons such as the class being moved to a different package, the class being renamed, the class being removed entirely, or the package itself could have been removed or renamed.

Without the specific details about the changes in the external dependency, I can't provide an exact code solution. However, I can give a general solution based on the common scenarios:

1. If the class has been moved to a different package, you would need to change the import statement to the new package location. For example, if the `IoCheckedScalar` class has been moved to the `org.cactoos` package, the import statement would change to:
```java
import org.cactoos.IoCheckedScalar;
```

2. If the class has been renamed, you would need to change the import statement to use the new class name. For example, if the `IoCheckedScalar` class has been renamed to `CheckedScalar`, the import statement would change to:
```java
import org.cactoos.scalar.CheckedScalar;
```

3. If the class has been removed entirely, you would need to find a replacement for that class in your code. This could be a different class provided by the same library, a class provided by a different library, or you may need to implement the functionality yourself. The changes in this case would be more extensive and would depend on the specific functionality provided by the `IoCheckedScalar` class.

4. If the package has been removed or renamed, you would need to update the import statement to reflect this. For example, if the `org.cactoos.scalar` package has been renamed to `org.cactoos.scalars`, the import statement would change to:
```java
import org.cactoos.scalars.IoCheckedScalar;
```

You would need to check the documentation or the source code of the `org.cactoos` library to find out the exact changes and update your code accordingly.