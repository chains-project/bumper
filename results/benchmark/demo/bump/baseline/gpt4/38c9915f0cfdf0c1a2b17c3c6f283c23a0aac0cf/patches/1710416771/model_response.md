It seems like the library `org.cactoos.iterable.LengthOf` is not found. This could be due to several reasons such as the library is not installed or the library has been updated and the class `LengthOf` is removed or renamed. 

Without knowing the exact version of the library you are using, it's hard to provide a specific solution. However, you can try to replace the `LengthOf` with alternative methods provided by the cactoos library or Java itself to calculate the length of an iterable.

Here is a sample code using Java Stream API:

```java
import java.util.stream.StreamSupport;

long length = StreamSupport.stream(iterable.spliterator(), false).count();
```

In the above code, `iterable` is the Iterable object that you want to calculate the length. Replace `iterable` with your actual object. This code creates a Stream from the Iterable and counts the number of elements.

Please replace the `iterable` with your actual object and insert this code to the place where you used `new LengthOf(iterable).value()`.