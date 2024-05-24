Here's a possible patch for the client code:
```java
import org.cactoos.text.UncheckedText;

// ...

public RtTransaction(String hash, TextTpl tpl, TextDao dao) {
  super(hash, new UncheckedText(tpl.asString()), dao);
}

// ...
```
The patch creates a new `UncheckedText` instance from the `tpl` object, which is an instance of `TextTpl`. This is possible because the `TextTpl` class implements the `Text` interface, which is a superinterface of `UncheckedText`.

The `UncheckedText` class is a new addition in the updated library version, and it provides a constructor that takes a `CharSequence` as an argument. This allows us to create an `UncheckedText` instance from the `String` returned by the `asString()` method of the `tpl` object.

By using `UncheckedText` instead of `SplitText`, we avoid the "cannot find symbol" error caused by the removal of the `SplitText` class.