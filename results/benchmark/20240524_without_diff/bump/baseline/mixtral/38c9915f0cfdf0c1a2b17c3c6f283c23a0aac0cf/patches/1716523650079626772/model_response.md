Here's the patched version of the client code that should fix the error:

```java
import org.cactoos.text.UncheckedText;

// ...

public class Remote {
 
    // ...

    @Override
    protected String text() {
        return new UncheckedText(new RandomText(10)).asString();
    }
}
```

In this patched version, I replaced the usage of `RandomText` with `UncheckedText`, which is a new class added in the updated library version. `UncheckedText` can take a `CharSequence` as a constructor argument, and we can create a `RandomText` instance that implements `CharSequence` to generate random text. This way, we can use the new library method to achieve the same functionality as the old `RandomText` class.