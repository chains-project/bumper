```java
  import org.cactoos.text.TrimmedText;
  import org.cactoos.text.UncheckedText;
  import org.cactoos.text.TextOf;

  public class RtTransaction {

    // ...

    public String getRt() {
      String rt = new UncheckedText(
          new TextOf(
              new TrimmedText(
                  this.rt
              )
          )
      ).asString();

      return rt;
    }

    // ...
  }
```