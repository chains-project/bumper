It seems like the library `org.cactoos.iterable.LengthOf` is not found. This could be due to a few reasons such as the library is not installed, the library is not in the classpath, or the library has been updated and the `LengthOf` class is no longer available or has been moved to a different package.

Without knowing the exact library and its version, it's hard to provide a precise solution. However, if the `LengthOf` class is removed or relocated, you should find an alternative way to achieve the same functionality.

Assuming `LengthOf` was used to get the length of an iterable, you can replace it with native Java code. Here is a patch using Java 8's Stream API:

```java
import java.util.stream.StreamSupport;

long length = StreamSupport.stream(iterable.spliterator(), false).count();
```

This code creates a stream from the iterable and counts the number of elements. Replace `iterable` with the actual iterable you were passing to `LengthOf`.