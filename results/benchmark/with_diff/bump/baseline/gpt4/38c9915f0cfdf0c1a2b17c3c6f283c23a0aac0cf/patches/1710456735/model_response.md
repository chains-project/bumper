It seems like the class `TrimmedText` has been removed from the package `org.cactoos.text`. Without the specific changes in the new library version, it's hard to provide an exact solution. However, typically, if a class like `TrimmedText` is removed, it's often replaced with a similar functionality in another class or method.

Here is a general way to fix it:

```java
  import org.cactoos.Text;
  import org.cactoos.text.TextOf;
  import org.cactoos.text.TextEnvelope;

  public final class Trimmed extends TextEnvelope {

      public Trimmed(final Text text) {
          super(new TextOf(text.asString().trim()));
      }
  }
```

In this code, we've created a new `Trimmed` class that extends `TextEnvelope` and trims the text in its constructor. This is assuming that the `TextEnvelope` and `TextOf` classes or similar ones are available in the new version of the library. 

Please replace the `TrimmedText` with this new `Trimmed` class in your main code. 

This is a general solution and might need adjustments based on the actual changes in the new library version.