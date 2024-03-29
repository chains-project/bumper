Here is a fixed version of the failing method in `WalletsIn.java`:
```java
import org.cactoos.text.Joined;

@Override
public String asString() throws IOException {
  return new Joined(SEPARATOR, inputs()).asString();
}
```
Note that I changed the import statement to use `org.cactoos.text.Joined` instead of `org.cactoos.text.JoinedText`. This is because the `JoinedText` class has been removed in the new version and replaced with `Joined`. The `Joined` class has the same method signatures as `JoinedText`, so the code should work the same way as before.