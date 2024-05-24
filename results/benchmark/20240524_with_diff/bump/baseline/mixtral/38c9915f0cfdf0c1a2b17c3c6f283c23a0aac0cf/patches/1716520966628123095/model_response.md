Here's a possible patch for the failing client code:
```java
import org.cactoos.bytes.IoCheckedBytes;

// ...

IoCheckedScalar<String> scalar = new IoCheckedScalar<>(() -> "Hello, world!");
IoCheckedBytes<String> bytes = new IoCheckedBytes<>(scalar::value);
String value = bytes.asBytes();
```
Explanation:
Since the `IoCheckedScalar` class has been removed in the new library version, we can no longer use it directly. However, we can achieve the same functionality by using the `IoCheckedBytes` class instead.
To do this, we first create an `IoCheckedScalar` instance using a lambda expression that returns the desired value.
Then, we create an `IoCheckedBytes` instance by passing the `scalar::value` method reference to its constructor. This effectively wraps the `IoCheckedScalar` instance in an `IoCheckedBytes` instance.
Finally, we can call the `asBytes()` method on the `IoCheckedBytes` instance to get the byte array representation of the original value.
Note that the type arguments for `IoCheckedScalar` and `IoCheckedBytes` are set to `String` in this example, but they can be changed to any other type as needed.