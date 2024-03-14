It seems like the import statement is causing the error. The class `LengthOf` could have been moved to a different package in the updated version of the cactoos library. Let's try to import it from `org.cactoos.collection` package instead:

```java
import org.cactoos.collection.LengthOf;
```