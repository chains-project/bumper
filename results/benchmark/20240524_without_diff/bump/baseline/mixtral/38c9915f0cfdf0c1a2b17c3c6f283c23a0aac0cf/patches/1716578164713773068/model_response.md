Here's the proposed patch to fix the error:

```java
import org.cactoos.text.Texts;
import org.cactoos.iterable.Joined;

// ...

@Override
public String all() throws IOException {
  return new Joined(Texts::trim, readers()).asString();
}
```

In this patch, I replaced the usage of `JoinedText` with `Joined`, which is an added library method identified with `++`. I also imported `Texts` and `Joined` classes from the `org.cactoos.text` package. The function signature remains unchanged.