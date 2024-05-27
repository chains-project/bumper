Here's the fixed version of the code:

```java
private org.hamcrest.Matcher<java.lang.String> layersPushed() {
    return org.hamcrest.MatcherAssert.not(org.hamcrest.CoreMatchers.stringContains(String.format("%s: Pushed", this.image.layer())));
}
```

This code uses the new `not` method from Hamcrest, which was added in the new library version. It's a replacement for the old `IsNot` class. The `stringContains` method is a shorthand for `StringContains` and is also a new addition.