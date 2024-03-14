It seems like the library `org.cactoos.iterable.LengthOf` is not found. This could be due to several reasons like the library not being present in the classpath, the library not being imported correctly, or the library not existing at all.

Without more information about the context and the use of this import in the code, it's hard to provide a specific solution. However, a common approach to deal with this issue is to check if the library is correctly added to your project dependencies. If it's not, you may need to add it.

If the library is correctly added and the import is still not found, then it might be possible that the class `LengthOf` does not exist in the `org.cactoos.iterable` package. In this case, you may need to replace the usage of this class with an equivalent one from the same or different library.

If the `LengthOf` class is used to get the length of an iterable, you could replace its usage with Java's native methods. For example, if you have a `Collection`, you can use its `size()` method. If you have an `Iterable`, you can convert it to a `Collection` and then get its size.

Without knowing the exact usage of the `LengthOf` class in your code, I can't provide a more specific solution. Here is a generic patch:

```java
import java.util.Collection;

// Replace the usage of LengthOf with Collection's size() method
Collection<?> yourCollection = // your iterable or collection
int length = yourCollection.size();
```

Please replace `yourCollection` with your actual collection or iterable.