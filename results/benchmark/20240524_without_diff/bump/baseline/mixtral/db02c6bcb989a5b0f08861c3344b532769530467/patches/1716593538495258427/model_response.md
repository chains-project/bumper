Here's a possible patch for the given code:

```java
  @Override
  public boolean matches(Object actual) {
    if (actual instanceof String) {
      String actualString = (String) actual;
      return actualString.contains(expected);
    }
    return false;
  }
```

In this patch, we first check if `actual` is an instance of `String`, and if so, we cast it to `String` and check if it contains `expected`. If `actual` is not a `String`, we immediately return `false`. This way, we avoid the need to cast `actual` to `String` twice, which could cause a `ClassCastException` if `actual` is not a `String`.