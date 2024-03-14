It seems like the library or the class `LengthOf` from `org.cactoos.iterable` cannot be found. This could be due to various reasons such as the library not being present in the classpath, the library not containing the class `LengthOf`, or the class has been moved to a different package in a newer version of the library.

If the library is not present in the classpath, you can add it using a dependency management tool like Maven or Gradle. If the class has been moved or renamed, you would need to find the new name or location and update the import statement accordingly.

Assuming that the class has been moved to a different package, you would need to update the import statement. Let's assume that the `LengthOf` class is now present in the `org.cactoos.collection` package. Here is the updated code:

```java
import org.cactoos.collection.LengthOf;
```

If the class has been removed completely, you would need to find an alternative way to achieve the same functionality. Without knowing the exact functionality of the `LengthOf` class, it's hard to provide a specific alternative. However, if it was used to get the length of an iterable, you could use the `size()` method of the iterable or convert the iterable to a collection and then use the `size()` method. The exact alternative would depend on your specific use case.

Please note that you need to verify the new location or alternative of the `LengthOf` class from the library documentation or source code.