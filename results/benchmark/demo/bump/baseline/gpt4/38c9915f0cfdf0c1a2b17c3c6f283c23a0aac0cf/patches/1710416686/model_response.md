The error message suggests that the symbol `LengthOf` from the package `org.cactoos.iterable` cannot be found. This could be due to a number of reasons such as: the package has been updated and the `LengthOf` class has been removed or moved to a different package, or the package is not correctly installed or imported in your project.

Without knowing the exact changes in the external dependency, it's difficult to propose a specific solution. However, a general approach to solve this issue could be to replace the usage of `LengthOf` with equivalent functionality provided by Java standard library.

Assuming `LengthOf` is used to get the length of an iterable, you could use the following code as a replacement:

```java
import java.util.stream.Collectors;
import java.util.stream.StreamSupport;

// Assuming iterable is an instance of Iterable
long length = StreamSupport.stream(iterable.spliterator(), false).count();
```

Please replace `iterable` with the actual instance of `Iterable` you have in your code.