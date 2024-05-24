Here is the proposed patch:
```java
import org.cactoos.text.TextEnvelope;

// ...

public RtTransaction(String id, TextEnvelope amount, TextEnvelope fee, TextEnvelope timestamp) {
  this.id = id;
  this.amount = amount;
  this.fee = fee;
  this.timestamp = timestamp;
}

// ...
```
Explanation:
The `TrimmedText` class has been removed from the library. Instead, we can use the `TextEnvelope` class, which provides a way to wrap a `Scalar` and convert it to a `Text`. This allows us to easily convert the `Scalar` to a `String` using the `asString()` method. By using `TextEnvelope`, we can ensure that the `Text` will never be null, which is a requirement for the `Text` class.

In the `RtTransaction` constructor, we can replace the `TrimmedText` instances with `TextEnvelope` instances. We can create a `TextEnvelope` by passing in a `Scalar` and using a lambda expression to convert the `Scalar` to a `String`.

By using `TextEnvelope` instead of `TrimmedText`, we can ensure that the code will work with the updated library version.