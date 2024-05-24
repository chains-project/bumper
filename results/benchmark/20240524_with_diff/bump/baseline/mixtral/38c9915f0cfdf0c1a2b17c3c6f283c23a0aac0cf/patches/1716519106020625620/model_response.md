Here's a possible patch for the client code:

```java
import org.cactoos.text.Joined;
import org.cactoos.text.Text;

...

Text joined = new Joined(" ", new Text[] { /* your text array */ });
```

In this patch, the `JoinedText` class has been removed and replaced with `Joined`. The usage of `Joined` is slightly different from `JoinedText`, as it takes an array of `Text` objects instead of a `CharSequence` and an `Iterable` of `Text` objects. You will need to adjust the initialization of the `Text` array according to your specific use case.