```java
  import org.cactoos.text.TrimmedText;
  import org.cactoos.text.UncheckedText;
  import org.cactoos.text.TextOf;

  public String trim(String text) {
    return new UncheckedText(new TrimmedText(new TextOf(text))).asString();
  }
```