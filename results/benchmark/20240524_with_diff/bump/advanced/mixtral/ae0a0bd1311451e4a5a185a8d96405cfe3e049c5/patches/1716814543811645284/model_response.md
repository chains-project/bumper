Here's the fixed version of the code:

```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.MatcherAssert.not(org.hamcrest.CoreMatchers.stringContains(String.format("%s: Pushed", this.image.layer())));
}
```

The failure was caused by the removal of the `IsNot` and `StringContains` classes from Hamcrest. They have been replaced by the `not` and `stringContains` methods in the `MatcherAssert` and `CoreMatchers` classes, respectively.