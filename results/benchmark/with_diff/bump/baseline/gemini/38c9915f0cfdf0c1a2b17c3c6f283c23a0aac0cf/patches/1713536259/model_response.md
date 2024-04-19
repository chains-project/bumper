```java
  import org.cactoos.scalar.StickyScalar;

  public String[] getWallets() {
    return new StickyScalar<>(
        () -> new String[]{
            "1",
            "2",
            "3",
        }
    ).value();
  }
```